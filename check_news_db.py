import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

async def check_news():
    load_dotenv(r"c:\Users\Admin\vjgc-final\vjs-website\.env")
    uri = os.getenv("MONGO_URI")
    client = AsyncIOMotorClient(uri)
    db = client["vjs_cms"]
    
    news_cats = ["Insights News", "News", "Media Release", "Insights / News"]
    
    print("--- Universal Content News ---")
    cursor = db["universal_content"].find({"category": {"$in": news_cats}})
    async for doc in cursor:
        print(f"Title: {doc.get('title')}, Category: {doc.get('category')}")
        
    print("\n--- 'news' Collection ---")
    cursor = db["news"].find()
    async for doc in cursor:
        print(f"Title: {doc.get('title')}, Author: {doc.get('author')}")

if __name__ == "__main__":
    asyncio.run(check_news())
