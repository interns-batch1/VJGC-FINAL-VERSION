import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check_all_home_content():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    print("--- HERO SECTION ---")
    async for doc in db["universal_content"].find({"mainPage": "home", "category": "Hero Section"}):
        print(f"Title: {doc.get('title')}, Image: {doc.get('image')}")
        
    print("\n--- INSIGHTS NEWS ---")
    async for doc in db["universal_content"].find({"mainPage": "home", "category": "Insights News"}):
        print(f"Title: {doc.get('title')}, Image: {doc.get('image')}")

    client.close()

if __name__ == "__main__":
    asyncio.run(check_all_home_content())
