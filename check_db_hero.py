import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

async def check_db():
    load_dotenv(r"c:\Users\Admin\vjgc-final\vjs-website\.env")
    uri = os.getenv("MONGO_URI")
    client = AsyncIOMotorClient(uri)
    db = client["vjs_cms"]
    
    cursor = db["universal_content"].find({"mainPage": "home", "category": "Hero Section"})
    async for doc in cursor:
        print(f"Title: {doc.get('title')}, SubSection: '{doc.get('subSection')}'")

if __name__ == "__main__":
    asyncio.run(check_db())
