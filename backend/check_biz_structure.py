import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def check():
    await connect_to_mongo()
    db = get_database()
    
    # Check one business page to see the structure
    docs = await db["universal_content"].find({
        "mainPage": "Business Verticals", 
        "subSection": "IT Consulting"
    }).to_list(length=10)
    
    for doc in docs:
        print(f"ID: {doc.get('_id')} | Cat: {doc.get('category')} | Title: {doc.get('title')}")
            
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(check())
