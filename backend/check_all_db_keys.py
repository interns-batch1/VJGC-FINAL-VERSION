import motor.motor_asyncio
import asyncio

async def check_all_keys():
    client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')
    db = client['vjs_cms']
    print("--- Database Content Keys ---")
    async for doc in db['universal_content'].find({}):
        print(f"ID: {doc.get('_id')}, Page: '{doc.get('mainPage')}', Sub: '{doc.get('subSection')}', Cat: '{doc.get('category')}', Title: '{doc.get('title')}'")

if __name__ == "__main__":
    asyncio.run(check_all_keys())
