import motor.motor_asyncio
import asyncio

async def find_trade():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    async for doc in db['universal_content'].find({"title": {"$regex": "Bridging Borders", "$options": "i"}}):
        print(doc)

if __name__ == "__main__":
    asyncio.run(find_trade())
