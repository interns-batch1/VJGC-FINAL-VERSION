import motor.motor_asyncio
import asyncio

async def find_heroes():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    print("--- Finding All Hero Section Documents ---")
    async for doc in db['universal_content'].find({"category": "Hero Section"}):
        print(f"mainPage: {doc.get('mainPage')}, subSection: {doc.get('subSection')}, title: {doc.get('title')}")

if __name__ == "__main__":
    asyncio.run(find_heroes())
