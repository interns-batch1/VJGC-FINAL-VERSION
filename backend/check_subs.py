
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("--- EXACT SUBSECTIONS FOR ABOUT US ---")
    async for d in db["universal_content"].find({"mainPage": "About Us"}):
        print(f"Sub: '{d.get('subSection')}'")

if __name__ == "__main__":
    asyncio.run(f())
