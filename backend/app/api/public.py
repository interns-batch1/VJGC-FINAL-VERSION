from fastapi import APIRouter, Depends
from app.db.mongodb import get_database
from datetime import datetime
from app.schemas.achievement import Achievement
from app.schemas.about import About
from app.schemas.service import Service
from app.schemas.blog import Blog
from typing import List, Optional

router = APIRouter()

@router.get("/about", response_model=About)
async def get_about(db = Depends(get_database)):
    """Fetch About Us content."""
    about = await db["about"].find_one()
    if about:
        about["_id"] = str(about["_id"])
    return about

@router.get("/achievements", response_model=List[Achievement])
async def list_achievements(db = Depends(get_database)):
    """List all achievements."""
    achievements = []
    cursor = db["achievements"].find().limit(100)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        achievements.append(doc)
    return achievements

@router.get("/services", response_model=List[Service])
async def list_services(db = Depends(get_database)):
    """List all services."""
    services = []
    cursor = db["services"].find().limit(100)
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        services.append(doc)
    return services

@router.get("/news", response_model=List[Blog])
async def list_news(db = Depends(get_database)):
    """List all news/blog posts from both 'news' and 'universal_content' collections."""
    import os
    print(f"DEBUG: list_news called in PID {os.getpid()}")
    cols = await db.list_collection_names()
    print(f"DEBUG: Collections in DB: {cols}")
    all_news = []
    seen_titles = set()
    
    # 1. Fetch from 'news' collection
    cursor = db["news"].find().sort("date", -1).limit(100)
    news_count = 0
    async for doc in cursor:
        news_count += 1
        doc["_id"] = str(doc["_id"])
        title = doc.get("title", "").strip().lower()
        if title:
            seen_titles.add(title)
        doc["source"] = "news_collection"
        all_news.append(doc)
        
    # 2. Fetch from 'universal_content' news categories
    news_categories = ["Insights News", "Latest_News", "News", "Media Release", "Insights / News", "News Section"]
    cursor = db["universal_content"].find({"category": {"$in": news_categories}}).sort("updatedAt", -1).limit(100)
    uni_count = 0
    async for doc in cursor:
        uni_count += 1
        title = doc.get("title", "").strip().lower()
        if title not in seen_titles:
            doc["_id"] = str(doc["_id"])
            if title:
                seen_titles.add(title)
            # Map universal fields to blog schema
            doc["date"] = doc.get("date") or doc.get("updatedAt").strftime("%Y-%m-%d") if doc.get("updatedAt") else "Recent"
            doc["status"] = "Published" if doc.get("isActive", True) else "Draft"
            doc["content"] = doc.get("content") or doc.get("description") or "No content available."
            doc["summary"] = doc.get("summary") or doc.get("description")
            doc["image_url"] = doc.get("image_url") or doc.get("image")
            doc["source"] = "universal_content"
            all_news.append(doc)
    
    print(f"DEBUG: Scanned {uni_count} universal items. Total unique news: {len(all_news)}")
    return all_news

@router.get("/news/{id}", response_model=Blog)
async def get_news_by_id(id: str, db = Depends(get_database)):
    """Fetch a single news item by ID."""
    from bson import ObjectId
    doc = await db["news"].find_one({"_id": ObjectId(id)})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc

@router.get("/cms/content", response_model=Optional[dict])
async def get_published_content(page: str, section: str, db = Depends(get_database)):
    """Fetch published CMS content for a specific page and section."""
    doc = await db["content"].find_one({"page": page, "section": section, "status": "published"})
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc
