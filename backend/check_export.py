import motor.motor_asyncio
import asyncio

async def check_export():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    print("--- Checking Export & Import ---")
    async for doc in db['universal_content'].find({"subSection": "Export & Import"}):
        print(doc)
    
    print("\n--- Checking Export&Import (no spaces) ---")
    async for doc in db['universal_content'].find({"subSection": "Export&Import"}):
        print(doc)

if __name__ == "__main__":
    asyncio.run(check_export())
