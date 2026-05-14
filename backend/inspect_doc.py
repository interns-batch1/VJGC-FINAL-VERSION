import motor.motor_asyncio
import asyncio

async def inspect_doc():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    doc = await db['universal_content'].find_one({"_id": "69fad04f51ab119f892ac592"}) # Wait, _id is likely an ObjectId
    from bson import ObjectId
    doc = await db['universal_content'].find_one({"_id": ObjectId("69fad04f51ab119f892ac592")})
    print(doc)

if __name__ == "__main__":
    asyncio.run(inspect_doc())
