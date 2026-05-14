
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- ABOUT US HERO ITEMS ---")
    query = {"mainPage": "About Us", "subSection": "About Group", "category": "Hero Section"}
    async for d in db["universal_content"].find(query):
        print(d)
    
    print("\n--- ALL ABOUT US ITEMS ---")
    async for d in db["universal_content"].find({"mainPage": "About Us"}):
        print(f"Sub: {d.get('subSection')} | Cat: {d.get('category')} | Title: {d.get('title')}")

if __name__ == "__main__":
    asyncio.run(f())
