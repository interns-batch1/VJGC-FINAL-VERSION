import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def find_code_video():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    print("Searching for 'Code.mp4' in all collections...")
    for coll_name in ["universal_content", "news"]:
        async for doc in db[coll_name].find({"image": {"$regex": "Code.mp4"}}):
            print(f"Collection: {coll_name}, Doc: {doc}")

    client.close()

if __name__ == "__main__":
    asyncio.run(find_code_video())
