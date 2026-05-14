import motor.motor_asyncio
import asyncio

async def check_hero():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    print("--- Checking Hero Section ---")
    query = {"mainPage": "About Us", "subSection": "About Group", "category": "Hero Section"}
    async for doc in db['universal_content'].find(query):
        print(f"ID: {doc.get('_id')}, Title: {doc.get('title')}, Subtitle: {doc.get('subtitle')}")

if __name__ == "__main__":
    asyncio.run(check_hero())
