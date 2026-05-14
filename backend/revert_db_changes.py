import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def revert_database_changes():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # 1. Revert video paths
    # Code.mp4
    await db["universal_content"].update_many(
        {"image": "Code.mp4"},
        {"$set": {"image": "/static/images/news_video/Code.mp4"}}
    )
    
    # scientist.mp4
    await db["universal_content"].update_many(
        {"image": "scientist.mp4"},
        {"$set": {"image": "/static/images/hero video/scientist-pours-chemicals-from-a-test-tube-into-a-2025-12-17-07-28-37-utc.mp4"}}
    )
    
    # farm.mp4
    await db["universal_content"].update_many(
        {"image": "farm.mp4"},
        {"$set": {"image": "/static/images/hero video/farm-agricultural-field-leveling-tractor-farm-work-2026-01-22-22-50-45-utc.mp4"}}
    )
    
    print("Database video paths reverted.")
    client.close()

if __name__ == "__main__":
    asyncio.run(revert_database_changes())
