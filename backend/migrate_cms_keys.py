import motor.motor_asyncio
import asyncio

async def migrate_keys():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    collection = db['universal_content']
    
    # 1. Migrate Main Pages
    await collection.update_many({"mainPage": "about"}, {"$set": {"mainPage": "About Us"}})
    await collection.update_many({"mainPage": "business"}, {"$set": {"mainPage": "Business Verticals"}})
    await collection.update_many({"mainPage": "newsroom"}, {"$set": {"mainPage": "Newsroom"}})
    await collection.update_many({"mainPage": "blog"}, {"$set": {"mainPage": "Blog"}})
    
    # 2. Migrate Sub-Sections
    await collection.update_many({"subSection": "about-group"}, {"$set": {"subSection": "About Group"}})
    await collection.update_many({"subSection": "journey"}, {"$set": {"subSection": "Our Journey"}})
    await collection.update_many({"subSection": "leadership"}, {"$set": {"subSection": "Leadership"}})
    await collection.update_many({"subSection": "awards"}, {"$set": {"subSection": "Awards"}})
    await collection.update_many({"subSection": "media-release"}, {"$set": {"subSection": "Media Release"}})
    
    # 4. Migrate Business Sub-Sections
    await collection.update_many({"subSection": "it-consulting"}, {"$set": {"subSection": "IT Consulting"}})
    await collection.update_many({"subSection": "data-centers"}, {"$set": {"subSection": "Enterprise Data Centers & Hosting Services"}})
    await collection.update_many({"subSection": "export-import"}, {"$set": {"subSection": "Export & Import"}})
    await collection.update_many({"subSection": "plantations"}, {"$set": {"subSection": "Plantations & Exotic Trees"}})
    await collection.update_many({"subSection": "it-training"}, {"$set": {"subSection": "IT Training"}})
    await collection.update_many({"subSection": "yoga-wellness"}, {"$set": {"subSection": "Yoga & Wellness"}})
    await collection.update_many({"subSection": "property-services"}, {"$set": {"subSection": "Property Services"}})
    await collection.update_many({"subSection": "green-energy"}, {"$set": {"subSection": "Green Energy & Solar Manufacturing"}})
    await collection.update_many({"subSection": "logistics"}, {"$set": {"subSection": "Logistics Services"}})
    await collection.update_many({"subSection": "travel-rentals"}, {"$set": {"subSection": "Travel & Rentals"}})
    
    # 3. Specifically fix Hero Section category casing if needed
    await collection.update_many({"category": "hero"}, {"$set": {"category": "Hero Section"}})
    await collection.update_many({"category": "Hero"}, {"$set": {"category": "Hero Section"}})

    print("Migration complete.")

if __name__ == "__main__":
    asyncio.run(migrate_keys())
