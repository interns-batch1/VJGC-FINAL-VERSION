import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

async def update_code_video_path():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # Update the document with Code.mp4
    result = await db["universal_content"].update_one(
        {"title": {"$regex": "Coding in the Modern Era"}},
        {"$set": {"image": "Code.mp4"}}
    )
    print(f"Updated Code.mp4 path: {result.modified_count}")

    client.close()

if __name__ == "__main__":
    asyncio.run(update_code_video_path())
