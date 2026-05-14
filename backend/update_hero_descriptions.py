import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"

async def update_hero_descriptions():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client["vjs_cms"]
    
    updates = [
        {
            "title": "Building Stronger Communities Together",
            "new_desc": "Community  Empowerment  Trust"
        },
        {
            "title": "Innovative Agricultural Solutions",
            "new_desc": "Agriculture Sustainability  Technology"
        },
        {
            "title": "Global Logistics and Supply Chain",
            "new_desc": "Logistics  Trade  Connectivity"
        },
        {
            "title": "Enterprise Business Consulting",
            "new_desc": "Innovation Excellence  Growth"
        },
        {
            "title": "Empowering Education & Skill Building",
            "new_desc": "Education  Skilling  Future"
        },
        {
            "title": "Eco-Friendly Industrial Breakthroughs",
            "new_desc": "Science  Research  Sustainability"
        },
        {
            "title": "Holistic Yoga & Wellness Programs",
            "new_desc": "Wellness  Health  Vitality"
        }
    ]
    
    for up in updates:
        result = await db.universal_content.update_many(
            {"title": up["title"], "mainPage": "home"},
            {"$set": {"description": up["new_desc"]}}
        )
        print(f"Updated '{up['title']}': Matched {result.matched_count}")

    client.close()

if __name__ == "__main__":
    asyncio.run(update_hero_descriptions())
