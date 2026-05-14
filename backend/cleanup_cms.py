
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def cleanup_and_sync():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Cleaning up redundant Hero/Content items...")
    
    # List of pages to fix
    pages = ["home", "About Us", "Business Verticals", "Newsroom", "Blog"]
    
    for page in pages:
        # 1. Rename 'Hero' to 'Hero Section' one by one to avoid collision
        async for doc in db["universal_content"].find({"category": "Hero", "mainPage": page}):
            try:
                await db["universal_content"].update_one(
                    {"_id": doc["_id"]},
                    {"$set": {"category": "Hero Section"}}
                )
                print(f"Updated Hero Slide in {page}: {doc.get('title')}")
            except Exception as e:
                print(f"Collision for {page} - {doc.get('title')}: {e}")
                # If collision, delete the duplicate
                await db["universal_content"].delete_one({"_id": doc["_id"]})
                print(f"Deleted duplicate Hero slide in {page}")

        # 2. Cleanup 'Content' category items (usually placeholders)
        r = await db["universal_content"].delete_many({"category": "Content"})
        if r.deleted_count > 0:
            print(f"Deleted {r.deleted_count} 'Content' category items.")

    print("Cleanup complete.")

if __name__ == "__main__":
    asyncio.run(cleanup_and_sync())
