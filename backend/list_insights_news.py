import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def check():
    await connect_to_mongo()
    db = get_database()
    
    items = await db["universal_content"].find({"category": "Insights News"}).sort("updatedAt", -1).to_list(length=20)
    for i, item in enumerate(items):
        print(f"{i+1}. Title: {item.get('title')} | Active: {item.get('isActive')} | Updated: {item.get('updatedAt')}")
            
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(check())
