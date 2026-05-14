import motor.motor_asyncio
import asyncio

async def check_it():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    print("--- Checking IT Training ---")
    async for doc in db['universal_content'].find({"subSection": "IT Training"}):
        print(doc)

if __name__ == "__main__":
    asyncio.run(check_it())
