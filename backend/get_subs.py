import asyncio
import os
import sys
sys.path.append(os.getcwd())
from app.db.mongodb import connect_to_mongo, get_database, close_mongo_connection

async def check():
    await connect_to_mongo()
    db = get_database()
    subs = await db['universal_content'].distinct('subSection', {'mainPage': 'Business Verticals'})
    print(subs)
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(check())
