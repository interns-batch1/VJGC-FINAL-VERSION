from fastapi import APIRouter, Depends, HTTPException, status
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.universal_content import UniversalContent, UniversalContentCreate, UniversalContentUpdate
from typing import List, Dict, Any, Optional
from datetime import datetime
from bson import ObjectId
import uuid

router = APIRouter()

# Mapping: slug sent by admin panel -> friendly name stored in MongoDB
SLUG_TO_NAME = {
    # Main pages
    "home":     "home",
    "about":    "About Us",
    "About Us": "About Us",
    "business": "Business Verticals",
    "Business Verticals": "Business Verticals",
    "newsroom": "Newsroom",
    "Newsroom": "Newsroom",
    "blog":     "Blog",
    "Blog":     "Blog",
    
    # Sub-sections (about)
    "about-group":  "About Group",
    "About Group":  "About Group",
    "leadership":   "Leadership",
    "Leadership":   "Leadership",
    "awards":       "Awards",
    "Awards":       "Awards",
    "journey":      "Our Journey",
    "Our Journey":  "Our Journey",
    
    # Sub-sections (newsroom)
    "media-release": "Media Release",
    "Media Release": "Media Release",
    
    # Sub-sections (business verticals)
    "it-consulting":      "IT Consulting",
    "data-centers":       "Enterprise Data Centers & Hosting Services",
    "export-import":      "Export & Import",
    "plantations":        "Plantations & Exotic Trees",
    "it-training":        "IT Training",
    "yoga-wellness":      "Yoga & Wellness",
    "property-services":  "Property Services",
    "green-energy":       "Green Energy & Solar Manufacturing",
    "logistics":          "Logistics Services",
    "travel-rentals":     "Travel & Rentals",
    
    # Categories
    "at-a-glance":    "At a Glance",
    "our-business":   "Our Business",
    "Hero Section":   "Hero Section",
    "Services":       "Services",
    "Insights / News": "Insights News",  # Normalized name
    "Insights News":  "Insights News",
    "Advisors":       "Advisors",
    "News":           "News",
}

def resolve(slug: Optional[str]) -> Optional[str]:
    """Translate a slug to its database-friendly name, or return as-is."""
    if slug is None:
        return None
    
    # Direct match first
    if slug in SLUG_TO_NAME:
        return SLUG_TO_NAME[slug]
        
    # Case-insensitive match
    lower_slug = slug.lower()
    for k, v in SLUG_TO_NAME.items():
        if k.lower() == lower_slug:
            return v
            
    return slug


# --- Static Structure Configuration ---
# This defines the UI dropdowns in the Admin Panel.
PAGES_CONFIG = {
    "home": [
        {"name": "Hero Section",    "label": "Hero Section",    "type": "hero"},
        {"name": "Services",        "label": "Services",        "type": "cards"},
        {"name": "Insights News", "label": "Insights News", "type": "news"},
    ],
    "About Us": {
        "About Group": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "Insights News", "label": "Insights News", "type": "news"}
        ],
        "Our Journey": [
            {"name": "Advisors", "label": "Advisors", "type": "cards"}
        ],
        "Leadership": [
            {"name": "Advisors", "label": "Advisors", "type": "cards"}
        ],
        "Awards": [
            {"name": "Awards", "label": "Awards", "type": "cards"}
        ]
    },
    "Business Verticals": {
        "IT Consulting": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Enterprise Data Centers & Hosting Services": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Export & Import": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Plantations & Exotic Trees": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "IT Training": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Yoga & Wellness": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Property Services": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Green Energy & Solar Manufacturing": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Logistics Services": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ],
        "Travel & Rentals": [
            {"name": "Hero Section", "label": "Hero Section", "type": "hero"},
            {"name": "At a Glance",  "label": "At a Glance",  "type": "cards"},
            {"name": "Our Business", "label": "Our Business", "type": "cards"}
        ]
    },
    "Newsroom": {
        "Media Release": [
            {"name": "News", "label": "News", "type": "news"}
        ]
    },
    "Blog": [
        {"name": "News", "label": "News", "type": "news"}
    ]
}


# ---------------------------------------------------------------------------
# GET /sections
# Called by Admin Panel when a page + sub-section is chosen.
# Returns the structural categories available to be edited.
# ---------------------------------------------------------------------------
@router.get("/sections")
async def get_sections(page: str = "home", subpage: Optional[str] = None):
    """Return the predefined categories for the selected page and subpage."""
    # Case-insensitive lookup for the main page config
    config = next((v for k, v in PAGES_CONFIG.items() if k.lower() == page.lower()), None)
    
    if not config:
        return []
        
    if isinstance(config, dict):
        if not subpage:
            return []
        # Case-insensitive lookup for sub-section config
        return next((v for k, v in config.items() if k.lower() == subpage.lower()), [])
        
    # If it's already a list, return it
    return config if isinstance(config, list) else []

# ---------------------------------------------------------------------------
# GET /all-categories
# Returns a list of distinct category names for the admin UI.
# ---------------------------------------------------------------------------
@router.get("/category-metadata")
async def get_all_categories(db = Depends(get_database)):
    """Retrieve unique combinations of mainPage, subSection, and category 
    along with the count of items in each.
    """
    pipeline = [
        # Filter out records missing critical fields
        {"$match": {"mainPage": {"$ne": None}, "category": {"$ne": None}}},
        {
            "$group": {
                "_id": {
                    "mainPage": "$mainPage",
                    "subSection": "$subSection",
                    "category": "$category"
                },
                "count": {"$sum": 1}
            }
        },
        {
            "$project": {
                "_id": 0,
                "mainPage": {"$ifNull": ["$_id.mainPage", ""]},
                "subSection": {"$ifNull": ["$_id.subSection", ""]},
                "category": {"$ifNull": ["$_id.category", ""]},
                "count": 1
            }
        },
        {"$sort": {"mainPage": 1, "subSection": 1, "category": 1}}
    ]
    results = []
    async for doc in db["universal_content"].aggregate(pipeline):
        results.append(doc)
    return results


@router.put("/categories/rename")
async def rename_category(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    """Rename a category across all records for a specific page/subsection."""
    old_main_page = data.get("oldMainPage")
    old_sub_section = data.get("oldSubSection") or ""
    old_category = data.get("oldCategory")
    new_category = data.get("newCategory")

    if not all([old_main_page, old_category, new_category]):
        raise HTTPException(status_code=400, detail="oldMainPage, oldCategory, and newCategory are required")

    result = await db["universal_content"].update_many(
        {"mainPage": old_main_page, "subSection": old_sub_section, "category": old_category},
        {"$set": {"category": new_category, "updatedAt": datetime.utcnow()}}
    )
    
    return {"message": f"Renamed {result.modified_count} items"}


@router.post("/categories/bulk-delete")
async def bulk_delete_category(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    """Delete all records in a specific category."""
    main_page = data.get("mainPage")
    sub_section = data.get("subSection") or ""
    category = data.get("category")

    if not all([main_page, category]):
        raise HTTPException(status_code=400, detail="mainPage and category are required")

    result = await db["universal_content"].delete_many(
        {"mainPage": main_page, "subSection": sub_section, "category": category}
    )
    
    return {"message": f"Deleted {result.deleted_count} items"}


# ---------------------------------------------------------------------------
# GET /content
# Called to load cards for the selected category.
# ---------------------------------------------------------------------------
@router.get("/content")
async def get_content(
    page:      Optional[str] = None,
    subpage:   Optional[str] = None,
    section:   Optional[str] = None,
    mainPage:  Optional[str] = None,
    subSection: Optional[str] = None,
    category:  Optional[str] = None,
    db = Depends(get_database)
):
    m = resolve(page or mainPage)
    s = resolve(subpage or subSection)
    c = resolve(section or category)

    print(f"DEBUG /content: m={m}, s={s}, c={c}")

    # --- List-all mode (used by Product List explorer) ---
    if not m and not s and not c:
        pipeline = [
            {"$group": {
                "_id": {"mainPage": "$mainPage", "subSection": "$subSection", "category": "$category"},
                "count":         {"$sum": 1},
                "last_modified": {"$max": "$updatedAt"},
                "is_active":     {"$first": "$isActive"}
            }}
        ]
        sections = []
        async for doc in db["universal_content"].aggregate(pipeline):
            sections.append({
                "_id":        f"{doc['_id']['mainPage']}-{doc['_id']['subSection']}-{doc['_id']['category']}",
                "page":       doc["_id"]["mainPage"],
                "subpage":    doc["_id"]["subSection"],
                "section":    doc["_id"]["category"],
                "status":     "published" if doc.get("is_active") else "draft",
                "type":       "cards",
                "updated_at": doc.get("last_modified"),
                "count":      doc["count"]
            })
        return sections

    # --- Specific content fetch ---
    query: Dict[str, Any] = {}
    if m: query["mainPage"]  = m
    if s: query["subSection"] = s
    if c: query["category"]  = c

    results = []
    async for doc in db["universal_content"].find(query).sort("order", 1):
        doc["_id"] = str(doc.pop("_id"))
        results.append(doc)

    print(f"DEBUG /content found {len(results)} items")

    # Infer section type from the category name so the admin renders correct fields
    hero_categories = {"Hero Section"}
    news_categories = {"Insights / News", "News Section", "News"}
    if c in hero_categories:
        section_type = "hero"
    elif c in news_categories:
        section_type = "news"
    else:
        section_type = "cards"

    return {
        "content": results,
        "type":    section_type,
        "id":      f"{m}-{s}-{c}"
    }


# ---------------------------------------------------------------------------
# PUT /content  (upsert a single item)
# ---------------------------------------------------------------------------
@router.put("/content")
async def upsert_content(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    mainPage   = resolve(data.get("mainPage"))
    subSection = resolve(data.get("subSection")) or ""   # Optional for Home/Blog
    category   = resolve(data.get("category"))

    if not all([mainPage, category]):
        raise HTTPException(status_code=400, detail="mainPage and category are required")

    doc = {
        "mainPage":   mainPage,
        "subSection": subSection,
        "category":   category,
        "updatedAt":  datetime.utcnow(),
        "isActive":   True
    }
    
    # Dynamically add all other fields (title, description, image, author, date, etc.)
    for k, v in data.items():
        if k not in ["_id", "mainPage", "subSection", "category", "updatedAt", "isActive"]:
            doc[k] = v

    await db["universal_content"].update_one(
        {"mainPage": mainPage, "subSection": subSection, "category": category, "title": data.get("title", "")},
        {"$set": doc, "$setOnInsert": {"createdAt": datetime.utcnow()}},
        upsert=True
    )
    return {"message": "Success"}


# ---------------------------------------------------------------------------
# POST /content  (upsert alias for the "Add to Collection" button)
# ---------------------------------------------------------------------------
@router.post("/content")
async def create_content(data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    """Upsert a single content item."""
    return await upsert_content(data, db, admin)


# ---------------------------------------------------------------------------
# PUT /content/{id}  (update by MongoDB _id)
# ---------------------------------------------------------------------------
@router.put("/content/{id}")
async def update_content_by_id(id: str, data: Dict[str, Any], db = Depends(get_database), admin: str = Depends(get_current_admin)):
    data.pop("_id", None)
    data["updatedAt"] = datetime.utcnow()
    
    # Ensure any slugs sent by the frontend are resolved back to DB friendly names
    if "mainPage" in data:   data["mainPage"]   = resolve(data["mainPage"])
    if "subSection" in data: data["subSection"] = resolve(data["subSection"])
    if "category" in data:   data["category"]   = resolve(data["category"])
        
    result = await db["universal_content"].update_one({"_id": ObjectId(id)}, {"$set": data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Updated"}


# ---------------------------------------------------------------------------
# PUT /content/{id}/publish
# Sets the content status to active/published.
# ---------------------------------------------------------------------------
@router.put("/content/{id}/publish")
async def publish_content(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["universal_content"].update_one(
        {"_id": ObjectId(id)},
        {"$set": {"isActive": True, "updatedAt": datetime.utcnow()}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Published successfully"}


# ---------------------------------------------------------------------------
# DELETE /content/{id}
# ---------------------------------------------------------------------------
@router.delete("/content/{id}")
async def delete_content(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    result = await db["universal_content"].delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Content not found")
    return {"message": "Deleted"}
    
# ---------------------------------------------------------------------------
# GET /activity
# Returns recent CMS activity for the dashboard
# ---------------------------------------------------------------------------
@router.get("/activity")
async def get_activity(db = Depends(get_database)):
    """Return the most recent CMS activity."""
    activities = []
    # Fetch the 10 most recently updated items
    cursor = db["universal_content"].find().sort("updatedAt", -1).limit(10)
    async for doc in cursor:
        activities.append({
            "id": str(doc["_id"]),
            "page": doc.get("mainPage", "Unknown"),
            "section": doc.get("category", "General"),
            "status": "published" if doc.get("isActive", True) else "draft",
            "updated_at": doc.get("updatedAt", datetime.utcnow()).isoformat()
        })
    return activities

