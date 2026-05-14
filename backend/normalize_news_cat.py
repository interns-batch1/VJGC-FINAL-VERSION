
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def f():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Normalizing 'Insights / News' to 'Insights News'...")
    r = await db["universal_content"].update_many(
        {"category": "Insights / News"},
        {"$set": {"category": "Insights News"}}
    )
    print(f"Updated: {r.modified_count} items")

if __name__ == "__main__":
    asyncio.run(f())
