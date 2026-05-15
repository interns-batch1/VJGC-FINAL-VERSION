import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

async def debug_list_news():
    load_dotenv(r"c:\Users\Admin\vjgc-final\vjs-website\.env")
    uri = os.getenv("MONGO_URI")
    client = AsyncIOMotorClient(uri)
    db = client["vjs_cms"]
    
    all_news = []
    seen_titles = set()
    
    # 1. Fetch from 'news' collection
    cursor = db["news"].find().sort("date", -1).limit(100)
    news_count = 0
    async for doc in cursor:
        news_count += 1
        title = doc.get("title", "").strip().lower()
        if title:
            seen_titles.add(title)
        all_news.append(doc)
    
    print(f"Items from 'news' collection: {news_count}")
        
    # 2. Fetch from 'universal_content' news categories
    news_categories = ["Insights News", "Latest_News", "News", "Media Release", "Insights / News", "News Section"]
    cursor = db["universal_content"].find({"category": {"$in": news_categories}}).sort("updatedAt", -1).limit(100)
    uni_count = 0
    added_count = 0
    async for doc in cursor:
        uni_count += 1
        title = doc.get("title", "").strip().lower()
        if title not in seen_titles:
            added_count += 1
            if title:
                seen_titles.add(title)
            all_news.append(doc)
            
    print(f"Universal items scanned: {uni_count}")
    print(f"Universal items added (non-duplicates): {added_count}")
    print(f"Total aggregated: {len(all_news)}")

if __name__ == "__main__":
    asyncio.run(debug_list_news())
