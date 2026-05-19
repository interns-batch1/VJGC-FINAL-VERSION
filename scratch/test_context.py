import asyncio
import os
import sys

# Add backend to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.db.mongodb import connect_to_mongo, close_mongo_connection
from app.main import get_page_context

async def main():
    await connect_to_mongo()
    context = await get_page_context("index-2")
    cms = context.get("cms", {})
    
    print("Keys in cms:")
    print(list(cms.keys()))
    
    if "Our Mission" in cms:
        print("\nOur Mission content:")
        print(cms["Our Mission"]["content"])
    else:
        print("\nOur Mission NOT in cms!")
        
    await close_mongo_connection()

if __name__ == "__main__":
    asyncio.run(main())
