import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

async def seed_notice():
    # Load env from backend directory
    load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
    mongo_uri = os.getenv("MONGO_URI")
    print(f"Connecting to {mongo_uri}")
    
    client = AsyncIOMotorClient(mongo_uri)
    db = client.get_database("vjs_cms")
    
    notice_data = {
        "mainPage": "home",
        "subSection": "",
        "category": "Notice",
        "title": "Important Notice",
        "description": "All official announcements, important alerts, and updates from Vijayalakshmi Group of Companies will be published and regularly updated through this section. We encourage everyone to refer only to our official communication channels for accurate and verified information. In the event of any misinformation, unauthorized activities, false claims, or any matter that may affect our customers, partners, employees, or the public, the Vijayalakshmi Group of Companies will provide timely notifications and necessary updates here. Please stay connected to this section to receive the latest official information, notices, and important company-related updates directly from Vijayalakshmi Group of Companies.",
        "isActive": True,
        "type": "text",
        "order": 0
    }
    
    # Check if exists
    existing = await db["universal_content"].find_one({"category": "Notice", "mainPage": "home"})
    if existing:
        print("Notice already exists. Updating...")
        await db["universal_content"].update_one(
            {"_id": existing["_id"]},
            {"$set": notice_data}
        )
    else:
        print("Creating new Notice...")
        await db["universal_content"].insert_one(notice_data)
    
    print("Done!")

if __name__ == "__main__":
    asyncio.run(seed_notice())
