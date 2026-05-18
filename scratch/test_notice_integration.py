import asyncio
import urllib.request
from motor.motor_asyncio import AsyncIOMotorClient

async def test_integration():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    client = AsyncIOMotorClient(uri)
    db = client[db_name]
    
    # 1. Fetch current notice
    notice = await db["universal_content"].find_one({"category": "Notice", "mainPage": "home"})
    if not notice:
        print("Error: No notice found in database to update!")
        return
        
    original_description = notice.get("description", "")
    print(f"Original Notice Title: '{notice.get('title')}'")
    print(f"Original Notice Desc snippet: '{original_description[:60]}...'")
    
    # 2. Update notice text to a test sentence
    test_text = "This is a custom test notice updated by Antigravity AI on 2026-05-18 to verify notice control works."
    await db["universal_content"].update_one(
        {"_id": notice["_id"]},
        {"$set": {"description": test_text, "title": "Important Notice Update"}}
    )
    print("Database notice document updated.")
    
    # 3. Request homepage and check if updated text exists
    try:
        response = urllib.request.urlopen("http://127.0.0.1:5006/").read().decode("utf-8")
        if test_text in response:
            print("SUCCESS: The updated notice was found on the live website home page!")
        else:
            print("FAILURE: The updated notice text was not found on the website homepage HTML.")
    except Exception as e:
        print(f"Error fetching website: {e}")
        
    # 4. Restore original notice text
    await db["universal_content"].update_one(
        {"_id": notice["_id"]},
        {"$set": {"description": original_description, "title": notice.get("title")}}
    )
    print("Database restored to original state.")

if __name__ == "__main__":
    asyncio.run(test_integration())
