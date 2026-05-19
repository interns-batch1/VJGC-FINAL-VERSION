from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import PlainTextResponse
from app.core.config import settings
from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.api import public, admin, auth, content, cms
from pathlib import Path
import os

app = FastAPI(title=settings.PROJECT_NAME)
print(f"DEBUG: MONGO_URI from settings: {settings.MONGO_URI}")


# Setup Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Custom StaticFiles subclass to enforce browser caching
class CachedStaticFiles(StaticFiles):
    def file_response(self, *args, **kwargs):
        response = super().file_response(*args, **kwargs)
        response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
        return response

# Serve static files
app.mount("/static", CachedStaticFiles(directory=str(BASE_DIR / "static")), name="static")

# Setup Templates
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# --- Compatibility Bridge for Flask Templates ---
from jinja2 import pass_context

@pass_context
def safe_url_for(context: dict, name: str, **params):
    request = context["request"]
    try:
        if name == "static" and "filename" in params:
            params["path"] = params.pop("filename")
        return str(request.url_for(name, **params))
    except Exception:
        return "#"

templates.env.globals["url_for"] = safe_url_for

# Global Error Handler
@app.exception_handler(Exception)
async def debug_exception_handler(request: Request, exc: Exception):
    import traceback
    print(f"DEBUG ERROR: {str(exc)}\n{traceback.format_exc()}")
    if request.url.path.startswith("/api"):
        from fastapi.responses import JSONResponse
        return JSONResponse(status_code=500, content={"detail": str(exc)})
    return templates.TemplateResponse(request, "index-2.html", await get_page_context("index-2"))

# Custom 404 Handler to prevent JSON responses for users, but allow API 404s
@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: Exception):
    if request.url.path.startswith("/api"):
        from fastapi.responses import JSONResponse
        return JSONResponse(status_code=404, content={"detail": "API endpoint not found"})
    return templates.TemplateResponse(request, "index-2.html", await get_page_context("index-2"))

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001",
        "http://localhost:5006",
        "https://vjgc-admin.vercel.app",
    ],
    allow_origin_regex="https://vjgc-admin-.*\\.vercel\\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static Files handled above with BASE_DIR
@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

# Include Routers
app.include_router(public.router, prefix="/api", tags=["Public"])
app.include_router(auth.router, prefix="/api/admin", tags=["Auth"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])
app.include_router(cms.router, prefix="/api/admin/cms", tags=["CMS"])
app.include_router(content.router, prefix="/api/content", tags=["Content Management"])

from app.db.mongodb import get_database

async def get_page_context(path: str):
    from app.core.cache import cms_cache
    import copy
    
    cached_val = cms_cache.get(path)
    if cached_val is not None:
        return copy.deepcopy(cached_val)
        
    db = get_database()
    context = {}
    
    if path == "index-2" or path == "":
        pass
        
    elif "about" in path:
        pass
            
    elif "service" in path:
        pass
        
    elif "news" in path or "blog" in path:
        pass
        
    # Fetch all published CMS content for this page/subpage
    # Map specific template paths to our CMS Main Page / Sub-Section structure
    path_map = {
        "": ("home", ""),
        "index-2": ("home", ""),
        "about-us-v2": ("About Us", "About Group"),
        "about-us-v1": ("About Us", "Our Journey"),
        "service-v1": ("About Us", "Leadership"),
        "media-release": ("Newsroom", "Media Release"),
        "media-kit": ("Newsroom", "Media Release"),
        "blog-v1": ("About Us", "Foundation"),
        # Business Verticals
        "data-centers-hosting": ("Business Verticals", "Enterprise Data Centers & Hosting Services"),
        "it-consulting": ("Business Verticals", "IT Consulting"),
        "green-energy": ("Business Verticals", "Green Energy & Solar Manufacturing"),
        "logistics-services": ("Business Verticals", "Logistics Services"),
        "export-import": ("Business Verticals", "Export & Import"),
        "property-services": ("Business Verticals", "Property Services"),
        "it-training": ("Business Verticals", "IT Training"),
        "yoga-wellness": ("Business Verticals", "Yoga & Wellness"),
        "travel-rentals": ("Business Verticals", "Travel & Rentals"),
        "plantations": ("Business Verticals", "Plantations & Exotic Trees"),
        "plantations-exotic-trees": ("Business Verticals", "Plantations & Exotic Trees"),
        # Sustainability Section
        "sustainability": ("Sustainability", "Main landing"),
        "digital-transformation-sustainability": ("Sustainability", "Digital Transformation & IT Consulting"),
        "cloud-infrastructure-sustainability": ("Sustainability", "Cloud, Hosting & Infrastructure"),
        "renewable-energy-solutions": ("Sustainability", "Renewable Energy Solutions"),
        "logistics-trade-sustainability": ("Sustainability", "Logistics & Trade Enablement"),
        "education-skill-sustainability": ("Sustainability", "Education & Skill Development"),
        "tree-plantation-sustainability": ("Sustainability", "Tree Plantation & Green Cover"),
        "eco-tech-solutions": ("Sustainability", "Eco-conscious Technology Solutions"),
        "renewable-energy-adoption": ("Sustainability", "Renewable Energy Adoption"),
        "sustainable-business-practices": ("Sustainability", "Sustainable Business Practices"),
        "educational-support-csr": ("Sustainability", "Educational Support"),
        "financial-material-aid": ("Sustainability", "Financial & Material Aid"),
        "skill-building-youth": ("Sustainability", "Skill-Building Programs"),
        "rural-semi-urban-engagement": ("Sustainability", "Rural & Semi-Urban Engagement"),
        "awareness-programs-community": ("Sustainability", "Awareness Programs"),
        "local-infrastructure-support": ("Sustainability", "Local Infrastructure Support")
    }
    
    # Normalize path
    clean_path = path
    if clean_path.endswith(".html"):
        clean_path = clean_path[:-5]
    if clean_path == "index":
        clean_path = ""
        
    page_name, sub_name = path_map.get(clean_path, (clean_path, ""))
    
    # Ensure sub_name is a string
    sub_name = sub_name or ""
    
    query = {"mainPage": {"$regex": f"^{page_name}$", "$options": "i"}, "isActive": True}
    if clean_path == "service-v1":
        query["subSection"] = {"$in": ["Leadership", "Awards"]}
    elif sub_name:
        query["subSection"] = sub_name
    else:
        # For pages without a specific subSection, match empty string or None
        query["subSection"] = {"$in": ["", None]}

    
    print(f"DEBUG: path='{path}' clean='{clean_path}' page='{page_name}' sub='{sub_name}'")
    print(f"DEBUG: query={query}")
    
    results = []
    async for doc in db["universal_content"].find(query).sort("order", 1):
        doc["_id"] = str(doc.pop("_id"))
        results.append(doc)
    
    print(f"DEBUG: Found {len(results)} results")
    
    class SafeDict(dict):
        def __getitem__(self, key):
            val = super().get(key, {"content": []})
            return val

    # Group by category
    cms_content = SafeDict()
    for doc in results:
        cat = doc.get("category", "General")
        if cat not in cms_content:
            cms_content[cat] = {"content": []}
        
        # Ensure template-friendly aliases
        img_path = doc.get("image") or ""
        if img_path:
            if img_path.startswith('/static/'):
                img_path = img_path.replace(' ', '%20')
            elif not img_path.startswith(('http', '/')):
                img_path = f"/uploads/{img_path}"
        doc["image_url"] = img_path
        doc["video_url"] = doc.get("video_url", img_path) if img_path.lower().endswith(".mp4") else ""
        
        cms_content[cat]["content"].append(doc)
        
    context["cms"] = cms_content

    # Dynamic SEO Metadata integration
    seo_defaults = {
        "": {
            "title": "Vijayalakshmi Group | Leading Sustainable Conglomerate",
            "description": "Vijayalakshmi Group of Companies is a premier global conglomerate specializing in Enterprise Data Centers, Green Energy, Logistics, IT Consulting, and Tree Plantations.",
            "keywords": "Green Energy, Data Centers, Logistics, VJS Group, IT Consulting, Tree Plantations, Vijayalakshmi Group",
            "og_title": "Vijayalakshmi Group of Companies | Sustainable Enterprise",
            "og_description": "Empowering sustainable growth across diverse business verticals globally.",
            "og_url": "https://vijayalakshmigroup.com/",
            "robots": "index, follow"
        },
        "index-2": {
            "title": "Vijayalakshmi Group | Leading Sustainable Conglomerate",
            "description": "Vijayalakshmi Group of Companies is a premier global conglomerate specializing in Enterprise Data Centers, Green Energy, Logistics, IT Consulting, and Tree Plantations.",
            "keywords": "Green Energy, Data Centers, Logistics, VJS Group, IT Consulting, Tree Plantations, Vijayalakshmi Group",
            "og_title": "Vijayalakshmi Group of Companies | Sustainable Enterprise",
            "og_description": "Empowering sustainable growth across diverse business verticals globally.",
            "og_url": "https://vijayalakshmigroup.com/",
            "robots": "index, follow"
        },
        "about-us-v1": {
            "title": "Our Journey | About Vijayalakshmi Group",
            "description": "Learn about the heritage, journey, and milestones of the Vijayalakshmi Group of Companies.",
            "keywords": "Our Journey, VJS Group History, Milestone, About Vijayalakshmi Group",
            "robots": "index, follow"
        },
        "about-us-v2": {
            "title": "About Group | Vijayalakshmi Group",
            "description": "Discover Vijayalakshmi Group of Companies' corporate history, core values, and vision.",
            "keywords": "About Group, Corporate Values, VJS Vision, Vijayalakshmi Group",
            "robots": "index, follow"
        },
        "service-v1": {
            "title": "Leadership & Awards | Vijayalakshmi Group",
            "description": "Meet our leadership team and explore the prestigious awards and recognition received by the Vijayalakshmi Group of Companies.",
            "keywords": "VJS Leadership, Group Awards, Corporate Recognition, Vijayalakshmi Group",
            "robots": "index, follow"
        },
        "green-energy": {
            "title": "Green Energy & Solar Manufacturing | Vijayalakshmi Group",
            "description": "Explore eco-friendly energy solutions and advanced solar manufacturing services by Vijayalakshmi Group of Companies.",
            "keywords": "Solar Manufacturing, Green Energy, Renewable Energy, Eco Friendly, Vijayalakshmi Group",
            "robots": "index, follow"
        },
        "data-centers-hosting": {
            "title": "Enterprise Data Centers & Hosting | Vijayalakshmi Group",
            "description": "Secure, scalable, and sustainable enterprise data center hosting and cloud infrastructure solutions by Vijayalakshmi Group.",
            "keywords": "Data Centers, Hosting Services, Cloud Infrastructure, Sustainable Hosting, Vijayalakshmi Group",
            "robots": "index, follow"
        },
        "it-consulting": {
            "title": "IT Consulting & Digital Transformation | Vijayalakshmi Group",
            "description": "Drive innovation and business optimization with elite IT consulting and enterprise systems design by Vijayalakshmi Group.",
            "keywords": "IT Consulting, Digital Transformation, Business Optimization, Software Services",
            "robots": "index, follow"
        },
        "logistics-services": {
            "title": "Logistics Services & Global Supply Chain | Vijayalakshmi Group",
            "description": "Safe, reliable, and integrated global supply chain and logistics services by Vijayalakshmi Group of Companies.",
            "keywords": "Logistics Services, Supply Chain, Cargo, Warehousing, Global Logistics",
            "robots": "index, follow"
        },
        "export-import": {
            "title": "Export & Import Global Trade | Vijayalakshmi Group",
            "description": "Facilitating seamless international trade and commodity export-import solutions across multiple sectors.",
            "keywords": "Export Import, Global Trade, Commodities, VJS Import Export",
            "robots": "index, follow"
        },
        "property-services": {
            "title": "Property Services & Asset Management | Vijayalakshmi Group",
            "description": "Premium real estate solutions, property development, and corporate asset management by Vijayalakshmi Group.",
            "keywords": "Property Services, Asset Management, Corporate Real Estate, Property Development",
            "robots": "index, follow"
        },
        "it-training": {
            "title": "IT Training & Professional Development | Vijayalakshmi Group",
            "description": "Empowering students and professionals with top-tier technology courses, certifications, and hands-on skill development.",
            "keywords": "IT Training, Professional Education, Skill Building, Tech Certification",
            "robots": "index, follow"
        },
        "yoga-wellness": {
            "title": "Yoga & Wellness Center | Vijayalakshmi Group",
            "description": "Promoting holistic health, mental clarity, and spiritual well-being through advanced yoga and wellness programs.",
            "keywords": "Yoga and Wellness, Holistic Health, VJS Yoga Center, Mindfulness",
            "robots": "index, follow"
        },
        "travel-rentals": {
            "title": "Travel & Premium Rentals | Vijayalakshmi Group",
            "description": "Hassle-free corporate car rentals, holiday planning, and premium tour operations by Vijayalakshmi Group.",
            "keywords": "Travel Rentals, Premium Tour, Car Rental, Corporate Travel, Holiday Planner",
            "robots": "index, follow"
        },
        "plantations": {
            "title": "Plantations & Exotic Trees | Vijayalakshmi Group",
            "description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
            "keywords": "Tree Plantation, Exotic Trees, Conservation, Green Cover, VJS Plantations",
            "robots": "index, follow"
        },
        "plantations-exotic-trees": {
            "title": "Plantations & Exotic Trees | Vijayalakshmi Group",
            "description": "Pioneering commercial plantations, sustainability conservation projects, and timber/horticultural cultivation.",
            "keywords": "Tree Plantation, Exotic Trees, Conservation, Green Cover, VJS Plantations",
            "robots": "index, follow"
        },
        "media-release": {
            "title": "Newsroom & Media Release | Vijayalakshmi Group",
            "description": "Stay updated with the latest press releases, corporate announcements, and insights from Vijayalakshmi Group of Companies.",
            "keywords": "Media Release, Press Release, VJS Newsroom, Corporate Insights",
            "robots": "index, follow"
        },
        "sustainability": {
            "title": "Sustainability & Corporate Social Responsibility | Vijayalakshmi Group",
            "description": "Discover the sustainability vision, environmental milestones, and community CSR initiatives of the Vijayalakshmi Group of Companies.",
            "keywords": "Sustainability VJS, CSR Initiatives, Green Business, Community Care",
            "robots": "index, follow"
        }
    }

    # Fetch customized SEO record from database, fallback to defaults
    seo_record = None
    try:
        seo_record = await db["seo_metadata"].find_one({"page_path": clean_path})
    except Exception as e:
        print(f"Error fetching SEO record for {clean_path}: {e}")

    if not seo_record:
        seo_record = seo_defaults.get(clean_path, {
            "title": "Vijayalakshmi Group of Companies",
            "description": "Official website of Vijayalakshmi Group of Companies.",
            "keywords": "Green Energy, Data Centers, Logistics, VJS Group",
            "robots": "index, follow"
        })
    else:
        seo_record["_id"] = str(seo_record["_id"])

    # Ensure OpenGraph elements exist
    seo_record["og_title"] = seo_record.get("og_title") or seo_record.get("title")
    seo_record["og_description"] = seo_record.get("og_description") or seo_record.get("description")
    seo_record["canonical_url"] = seo_record.get("canonical_url")
    seo_record["robots"] = seo_record.get("robots") or "index, follow"

    context["seo"] = seo_record

    # Save calculated context to the in-memory cache
    cms_cache.set(path, copy.deepcopy(context))
    
    return context

@app.get("/blog-details/{id}", name="blog_details")
async def blog_details(request: Request, id: str):
    from app.db.mongodb import get_database
    from bson import ObjectId
    db = get_database()
    
    blog = None
    try:
        # Try finding in news collection first
        blog = await db["news"].find_one({"_id": ObjectId(id)})
        if not blog:
            # Fallback to universal_content
            blog = await db["universal_content"].find_one({"_id": ObjectId(id)})
            
        if blog:
            blog["_id"] = str(blog["_id"])
    except Exception as e:
        print(f"Error fetching blog {id}: {e}")
        
    context = await get_page_context("blog-details")
    
    # Prepare sidebar news: prioritize 'Vijayalakshmi Groups' page news (Insights News)
    all_news = []
    seen_ids = {str(id)}
    
    # 1. Add CMS News categories
    news_categories = ["Insights News", "Latest_News", "News", "Insights / News", "News Section"]
    for cat in news_categories:
        cat_items = await db["universal_content"].find({"category": cat, "isActive": True}).sort("updatedAt", -1).to_list(length=50)
        for n in cat_items:
            if str(n["_id"]) not in seen_ids:
                n["_id"] = str(n["_id"])
                all_news.append(n)
                seen_ids.add(str(n["_id"]))
                
    # 2. Add blog news (Media Releases)
    for n in context.get("recent_blog_news", []):
        if str(n["_id"]) not in seen_ids:
            all_news.append(n)
            seen_ids.add(str(n["_id"]))
            
    context["sidebar_news"] = all_news[:7]
    context["blog"] = blog
    
    if not blog:
        # If blog still not found, redirect to newsroom or show home
        return templates.TemplateResponse(request, "media-release.html", await get_page_context("media-release"))

    return templates.TemplateResponse(request, "blog-details.html", context)

# Serve Website Pages
@app.get("/", name="home")
async def home(request: Request):
    context = await get_page_context("index-2")
    return templates.TemplateResponse(request, "index-2.html", context)

@app.get("/{path}", name="dynamic_route")
async def dynamic_route(request: Request, path: str):
    try:
        clean_path = path.replace(".html", "")
        if clean_path == "blog-details":
            from fastapi.responses import RedirectResponse
            return RedirectResponse(url="/media-release")
            
        template_file = f"{clean_path}.html"
        context = await get_page_context(clean_path)
        
        # Special handling for media-release to include ALL news sources
        if clean_path == "media-release":
            db = get_database()
            all_media = []
            seen_ids = set()
            seen_titles = set()
            
            # 1. Add from 'news' collection (Website News)
            try:
                news_items = await db["news"].find().sort("date", -1).to_list(length=50)
                for n in news_items:
                    nid = str(n["_id"])
                    title = n.get("title", "").strip().lower()
                    if nid not in seen_ids and title not in seen_titles:
                        n["_id"] = nid
                        if "image" in n:
                            img = n["image"]
                            if img and not img.startswith(('http', '/', 'static/')):
                                img = f"/uploads/{img}"
                            if img and img.startswith('/static/'):
                                img = img.replace(' ', '%20')
                            n["image_url"] = img
                        all_media.append(n)
                        seen_ids.add(nid)
                        if title: seen_titles.add(title)
            except Exception as e:
                print(f"Error fetching from news collection: {e}")

            # 2. Add CMS News categories (Admin Panel News)
            news_categories = ["Insights News", "Latest_News", "News", "Media Release", "Insights / News", "News Section"]
            for cat in news_categories:
                try:
                    cat_items = await db["universal_content"].find({"category": cat, "isActive": True}).sort("updatedAt", -1).to_list(length=30)
                    for n in cat_items:
                        nid = str(n["_id"])
                        title = n.get("title", "").strip().lower()
                        if nid not in seen_ids and title not in seen_titles:
                            n["_id"] = nid
                            if "image" in n:
                                img = n["image"]
                                if img and not img.startswith(('http', '/', 'static/')):
                                    img = f"/uploads/{img}"
                                if img and img.startswith('/static/'):
                                    img = img.replace(' ', '%20')
                                n["image_url"] = img
                            all_media.append(n)
                            seen_ids.add(nid)
                            if title: seen_titles.add(title)
                except Exception as e:
                    print(f"Error fetching {cat} from universal_content: {e}")
            
            # Sort all combined news by date if available, else updatedAt
            def get_sort_key(x):
                val = x.get("date") or x.get("updatedAt") or ""
                if hasattr(val, 'isoformat'):
                    return val.isoformat()
                return str(val)

            all_media.sort(key=get_sort_key, reverse=True)
            context["all_media_news"] = all_media
            
        return templates.TemplateResponse(request, template_file, context)
    except Exception as e:
        import traceback
        print(f"ERROR rendering {path}: {str(e)}\n{traceback.format_exc()}")
        return templates.TemplateResponse(request, "index-2.html", await get_page_context("index-2"))
