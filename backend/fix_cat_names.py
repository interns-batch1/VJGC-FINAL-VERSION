
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def fix_categories():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Renaming category 'Hero' to 'Hero Section'...")
    r = await db["universal_content"].update_many(
        {"category": "Hero"},
        {"$set": {"category": "Hero Section"}}
    )
    print(f"Updated: {r.modified_count} items")

    print("Renaming category 'Content' to 'Hero Section' (if it was meant for Hero)...")
    # Some items might have been saved as 'Content' by mistake
    r = await db["universal_content"].update_many(
        {"category": "Content", "mainPage": "About Us"},
        {"$set": {"category": "Hero Section"}}
    )
    print(f"Updated: {r.modified_count} items")

if __name__ == "__main__":
    asyncio.run(fix_categories())
