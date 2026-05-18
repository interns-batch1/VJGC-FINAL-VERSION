import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def cleanup_notices():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    print("Fetching all Notice documents...")
    cursor = db["universal_content"].find({"category": "Notice", "mainPage": "home"}).sort("updatedAt", -1)
    notices = []
    async for doc in cursor:
        notices.append(doc)
        
    print(f"Found {len(notices)} notices.")
    
    if len(notices) > 1:
        # Keep the first one (most recently updated)
        keep_id = notices[0]["_id"]
        print(f"Keeping notice with ID: {keep_id} (Title: '{notices[0].get('title')}')")
        
        # Delete the others
        for n in notices[1:]:
            delete_id = n["_id"]
            print(f"Deleting duplicate notice with ID: {delete_id} (Title: '{n.get('title')}')")
            await db["universal_content"].delete_one({"_id": delete_id})
            
        print("Duplicate notices cleaned up successfully.")
    elif len(notices) == 1:
        print("Only one notice exists, no cleanup needed.")
    else:
        print("No notices found. Re-seeding one default notice...")
        notice_data = {
            "mainPage": "home",
            "subSection": "",
            "category": "Notice",
            "title": "Important Notice",
            "description": "All official announcements, important alerts, and updates from Vijayalakshmi Group of Companies will be published and regularly updated through this section. We encourage everyone to refer only to our official communication channels for accurate and verified information. In the event of any misinformation, unauthorized activities, false claims, or any matter that may affect our customers, partners, employees, or the public, the Vijayalakshmi Group of Companies will provide timely notifications and necessary updates here. Please stay connected to this section to receive the latest official information, notices, and important company-related updates directly from Vijayalakshmi Group of Companies.",
            "isActive": True,
            "type": "text",
            "order": 0
        }
        await db["universal_content"].insert_one(notice_data)
        print("Default notice seeded.")

if __name__ == "__main__":
    asyncio.run(cleanup_notices())
