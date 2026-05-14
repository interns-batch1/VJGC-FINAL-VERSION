import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

async def deactivate_extra_cards():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # 1. Deactivate 'Sustainable Agriculture' (Tractor duplicate)
    await db["universal_content"].update_one(
        {"title": {"$regex": "Sustainable Agriculture"}},
        {"$set": {"isActive": False}}
    )
    
    # 2. Deactivate 'Scientific Breakthroughs' (Scientist video)
    await db["universal_content"].update_one(
        {"title": {"$regex": "Scientific Breakthroughs"}},
        {"$set": {"isActive": False}}
    )

    print("Extra cards deactivated. Keeping Global Expansion and Sustainable Energy (Tractor).")
    client.close()

if __name__ == "__main__":
    asyncio.run(deactivate_extra_cards())
