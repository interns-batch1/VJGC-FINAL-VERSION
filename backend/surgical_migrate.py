import motor.motor_asyncio
import asyncio

async def surgical_migrate():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    collection = db['universal_content']
    
    # Mapping old subSection names to new ones
    mappings = {
        "Education": "IT Training",
        "Technology": "IT Consulting",
        "Energy": "Green Energy & Solar Manufacturing",
        "Transport": "Logistics Services",
        "Consumer": "Export & Import",
        "Real Estate": "Property Services",
        "Healthcare": "Yoga & Wellness",
        "Finance": "Export & Import", # Fallback if unknown
        "Hospitality": "Travel & Rentals",
        "journey": "Our Journey",
        "About Group": "About Group" # Already standardized but for safety
    }
    
    for old, new in mappings.items():
        try:
            res = await collection.update_many({"subSection": old}, {"$set": {"subSection": new}})
            print(f"Migrated {old} -> {new}: {res.modified_count} docs")
        except Exception as e:
            print(f"Error migrating {old} -> {new}: {str(e)}")
            # Try updating one by one to skip duplicates
            async for doc in collection.find({"subSection": old}):
                try:
                    await collection.update_one({"_id": doc["_id"]}, {"$set": {"subSection": new}})
                except:
                    pass
            print(f"Finished fallback migration for {old}")
    
    # Also fix lowercase ones just in case
    await collection.update_many({"subSection": "it-training"}, {"$set": {"subSection": "IT Training"}})
    await collection.update_many({"subSection": "yoga-wellness"}, {"$set": {"subSection": "Yoga & Wellness"}})

    print("Surgical migration complete.")

if __name__ == "__main__":
    asyncio.run(surgical_migrate())
