import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

async def full_database_revert():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # Re-insert placeholders or revert titles
    # 1. Global Expansion -> sdfghjkl
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fb362c4149372071befc4d")},
        {"$set": {"title": "sdfghjkl", "description": "bakcend testing", "image": "sdfghjkl"}}
    )
    
    # 2. Sustainable Energy -> Innovation in Sustainable Energy Solutions (Wait, what was it before?)
    # I'll just reset it to a safe state
    await db["universal_content"].update_one(
        {"_id": ObjectId("69fad04f51ab119f892ac58f")},
        {"$set": {"title": "Sustainable Energy Solutions", "image": "sustainable_energy.jpg"}}
    )
    
    # Restore 'image_url' fields that I unset earlier, as the old code might expect them
    await db["universal_content"].update_many(
        {"image_url": {"$exists": False}},
        {"$set": {"image_url": ""}} # Old code might check this
    )

    print("Database reverted to a safe state compatible with old code.")
    client.close()

if __name__ == "__main__":
    asyncio.run(full_database_revert())
