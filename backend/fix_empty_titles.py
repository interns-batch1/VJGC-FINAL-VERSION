import motor.motor_asyncio
import asyncio

async def fix_empty_titles():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    collection = db['universal_content']

    # Fix Journey
    await collection.update_one(
        {"mainPage": "About Us", "subSection": "Journey", "category": "Hero Section"},
        {"$set": {"title": "A Trusted Name Across Multiple Industries"}}
    )
    print("Fixed Journey Title")

    # Fix Awards
    await collection.update_one(
        {"mainPage": "About Us", "subSection": "Awards", "category": "Hero Section"},
        {"$set": {"title": "Leadership & Excellence"}}
    )
    print("Fixed Awards Title")

if __name__ == "__main__":
    asyncio.run(fix_empty_titles())
