import motor.motor_asyncio
import asyncio

async def check_db():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['vjs_cms']
    print("--- About Us Content ---")
    async for doc in db['universal_content'].find({"mainPage": {"$regex": "About", "$options": "i"}}):
        print(f"Page: {doc.get('mainPage')}, Sub: {doc.get('subSection')}, Cat: {doc.get('category')}, Title: {doc.get('title')}")

if __name__ == "__main__":
    asyncio.run(check_db())
