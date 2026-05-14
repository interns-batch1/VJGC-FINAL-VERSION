
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Syncing 'Journey' to 'Our Journey'...")
    r = await db["universal_content"].update_many(
        {"subSection": "Journey"},
        {"$set": {"subSection": "Our Journey"}}
    )
    print(f"Updated: {r.modified_count} items")

if __name__ == "__main__":
    asyncio.run(f())
