import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

async def diversify_videos():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # Set 'Sustainable Energy Solutions' to use the Farm/Agriculture video
    # Since 'Scientific Breakthroughs' is using the Scientist video.
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fad04f51ab119f892ac58f")},
        {"$set": {
            "image": "/static/images/hero video/farm-agricultural-field-leveling-tractor-farm-work-2026-01-22-22-50-45-utc.mp4"
        }}
    )

    print("Sustainable Energy Solutions updated to use the Agriculture video for diversity.")
    client.close()

if __name__ == "__main__":
    asyncio.run(diversify_videos())
