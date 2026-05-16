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

# Serve static files
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")

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
    allow_origins=["*"],
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
        "blog-v1": ("Blog", ""),
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
        "plantations-exotic-trees": ("Business Verticals", "Plantations & Exotic Trees")
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
    if sub_name:
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
