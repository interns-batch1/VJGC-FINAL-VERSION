
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def sync_database_names():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Syncing database to new naming convention...")
    
    # 1. About -> About Us
    r = await db["universal_content"].update_many(
        {"mainPage": "About"},
        {"$set": {"mainPage": "About Us"}}
    )
    print(f"Updated 'About' to 'About Us': {r.modified_count} items")

    # 2. Home -> home (lowercase)
    r = await db["universal_content"].update_many(
        {"mainPage": "Home"},
        {"$set": {"mainPage": "home"}}
    )
    print(f"Updated 'Home' to 'home': {r.modified_count} items")

    # 3. subSection cleanup (just in case)
    # The user is now using "About Group", "Our Journey", "Leadership", "Awards"
    # My previous migration already used "About Group" for News, but let's be sure for others.
    
    # Also handle Business Verticals sub-sections if they changed
    # User's AddProduct.tsx uses "IT Consulting", "Enterprise Data Centers & Hosting Services", etc.
    # Let's check what's in the DB.
    
    # I'll also do a case-insensitive check for common sub-sections
    sub_map = {
        "about-group": "About Group",
        "journey": "Our Journey",
        "leadership": "Leadership",
        "awards": "Awards",
        "it-consulting": "IT Consulting",
        "data-centers": "Enterprise Data Centers & Hosting Services",
        "export-import": "Export & Import",
        "plantations": "Plantations & Exotic Trees",
        "it-training": "IT Training",
        "yoga-wellness": "Yoga & Wellness",
        "property-services": "Property Services",
        "green-energy": "Green Energy & Solar Manufacturing",
        "logistics": "Logistics Services",
        "travel-rentals": "Travel & Rentals"
    }
    
    for old, new in sub_map.items():
        r = await db["universal_content"].update_many(
            {"subSection": old},
            {"$set": {"subSection": new}}
        )
        if r.modified_count > 0:
            print(f"Updated subSection '{old}' to '{new}': {r.modified_count} items")

    print("Sync complete.")

if __name__ == "__main__":
    asyncio.run(sync_database_names())
