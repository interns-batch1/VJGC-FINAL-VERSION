import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def list_all_news():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    print("--- ALL INSIGHTS NEWS ---")
    async for doc in db["universal_content"].find({"category": "Insights News"}):
        print(f"Title: {doc.get('title')}, Image: {doc.get('image')}, Active: {doc.get('isActive')}, Page: {doc.get('mainPage')}")

    client.close()

if __name__ == "__main__":
    asyncio.run(list_all_news())
