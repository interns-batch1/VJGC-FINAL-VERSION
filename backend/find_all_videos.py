import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def find_all_videos():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    print("--- ALL VIDEO DOCUMENTS ---")
    async for doc in db["universal_content"].find({"image": {"$regex": "\.mp4$"}}):
        print(f"Title: {doc.get('title')}, Image: {doc.get('image')}, Active: {doc.get('isActive')}, Page: {doc.get('mainPage')}")

    client.close()

if __name__ == "__main__":
    asyncio.run(find_all_videos())
