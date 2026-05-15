import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

async def check_dbs():
    load_dotenv(r"c:\Users\Admin\vjgc-final\vjs-website\.env")
    uri = os.getenv("MONGO_URI")
    client = AsyncIOMotorClient(uri)
    dbs = await client.list_database_names()
    print(f"Databases: {dbs}")
    
    for db_name in dbs:
        db = client[db_name]
        cols = await db.list_collection_names()
        print(f"  {db_name} collections: {cols}")
        if "universal_content" in cols:
            count = await db["universal_content"].count_documents({})
            print(f"    universal_content count: {count}")
        if "news" in cols:
            count = await db["news"].count_documents({})
            print(f"    news count: {count}")

if __name__ == "__main__":
    asyncio.run(check_dbs())
