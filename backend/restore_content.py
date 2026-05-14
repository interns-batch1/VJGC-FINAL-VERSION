import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

async def restore_good_content():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # 1. Restore News Cards
    # Global Expansion
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fb362c4149372071befc4d")},
        {"$set": {
            "title": "Global Expansion: New Strategic Partnerships",
            "description": "Strengthening our international presence through collaborative ventures across key growth markets.",
            "image": "/static/images/hero video/freight-transport-2025-12-17-20-47-07-utc.mp4",
            "isActive": True
        }}
    )
    
    # Sustainable Energy
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fad04f51ab119f892ac58f")},
        {"$set": {
            "title": "Innovation in Sustainable Energy Solutions",
            "description": "Pioneering new solar and renewable technologies to power a greener future.",
            "image": "/static/images/hero video/scientist-pours-chemicals-from-a-test-tube-into-a-2025-12-17-07-28-37-utc.mp4",
            "isActive": True
        }}
    )
    
    # Coding / Technology
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fb15e9fd422f7f6c702e9b")},
        {"$set": {
            "image": "/static/images/news_video/Code.mp4",
            "isActive": True
        }}
    )

    print("Professional content and video paths restored in database.")
    client.close()

if __name__ == "__main__":
    asyncio.run(restore_good_content())
