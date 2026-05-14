import motor.motor_asyncio
import asyncio

async def fix_plantation_hero():
    uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    client = motor.motor_asyncio.AsyncIOMotorClient(uri)
    db = client['vjs_cms']
    collection = db['universal_content']

    # Update the record that has title "Consumer" and subSection "Plantations & Exotic Trees"
    await collection.update_one(
        {"mainPage": "Business Verticals", "subSection": "Plantations & Exotic Trees", "category": "Hero Section"},
        {"$set": {
            "title": "Cultivating Green Wealth<br>For Generations.",
            "description": "Spanning 10,000+ acres of exotic tree plantations, we are dedicated to sustainable forestry and ecological conservation.",
            "image": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&q=80&w=1200"
        }}
    )
    print("Fixed Plantation Hero Record")

if __name__ == "__main__":
    asyncio.run(fix_plantation_hero())
