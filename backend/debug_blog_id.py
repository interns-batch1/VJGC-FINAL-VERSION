import asyncio
from app.db.mongodb import connect_to_mongo, get_database
from bson import ObjectId

async def debug_blog(id_str):
    await connect_to_mongo()
    db = get_database()
    print(f"Searching for ID: {id_str}")
    
    try:
        obj_id = ObjectId(id_str)
        # Check news
        news = await db["news"].find_one({"_id": obj_id})
        if news:
            print(f"Found in 'news' collection: {news.get('title')}")
        else:
            print("Not found in 'news'")
            
        # Check universal_content
        universal = await db["universal_content"].find_one({"_id": obj_id})
        if universal:
            print(f"Found in 'universal_content' collection: {universal.get('title')}")
        else:
            print("Not found in 'universal_content'")
            
    except Exception as e:
        print(f"Error parsing ObjectId: {e}")

if __name__ == "__main__":
    import sys
    target_id = sys.argv[1] if len(sys.argv) > 1 else "69fb15eafd422f7f6c702ea1"
    asyncio.run(debug_blog(target_id))
