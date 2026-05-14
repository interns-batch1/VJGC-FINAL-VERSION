import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def fix_all_video_paths():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = AsyncIOMotorClient(mongo_uri)
    db = client["vjs_cms"]
    
    # Map old paths to new filenames in uploads
    mapping = {
        "scientist-pours-chemicals": "scientist.mp4",
        "farm-agricultural-field": "farm.mp4",
        "Code.mp4": "Code.mp4"
    }
    
    for old_part, new_name in mapping.items():
        result = await db["universal_content"].update_many(
            {"image": {"$regex": old_part}},
            {"$set": {"image": new_name}}
        )
        print(f"Updated {old_part} -> {new_name}: {result.modified_count} items")

    client.close()

if __name__ == "__main__":
    asyncio.run(fix_all_video_paths())
