import motor.motor_asyncio
import asyncio
from datetime import datetime

async def seed_missing_heroes():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    collection = db['universal_content']

    missing_heroes = [
        {
            "mainPage": "Business Verticals",
            "subSection": "Export & Import",
            "category": "Hero Section",
            "title": "Bridging Borders<br>With Global Trade.",
            "description": "Simplifying complex international trade through expert import-export services and a robust global supply chain network.",
            "image": "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&q=80&w=1200",
            "isActive": True,
            "order": 0,
            "createdAt": datetime.utcnow()
        },
        {
            "mainPage": "Business Verticals",
            "subSection": "Logistics Services",
            "category": "Hero Section",
            "title": "Moving the World<br>With Precision.",
            "description": "Delivering end-to-end logistics and mobility solutions that power global supply chains with speed and reliability.",
            "image": "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&q=80&w=1200",
            "isActive": True,
            "order": 0,
            "createdAt": datetime.utcnow()
        }
    ]

    for hero in missing_heroes:
        # Check if exists
        existing = await collection.find_one({
            "mainPage": hero["mainPage"],
            "subSection": hero["subSection"],
            "category": hero["category"]
        })
        if not existing:
            await collection.insert_one(hero)
            print(f"Inserted Hero for {hero['subSection']}")
        else:
            print(f"Hero for {hero['subSection']} already exists")

if __name__ == "__main__":
    asyncio.run(seed_missing_heroes())
