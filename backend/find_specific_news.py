import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def check():
    await connect_to_mongo()
    db = get_database()
    
    # Search for specific titles to find their categories
    titles = ["Aditya Institute", "Agham Grham"]
    for title in titles:
        doc = await db["universal_content"].find_one({"title": {"$regex": title, "$options": "i"}})
        if doc:
            print(f"Found '{title}' in category: {doc.get('category')}")
        else:
            print(f"Did not find '{title}' in universal_content")
            
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(check())
