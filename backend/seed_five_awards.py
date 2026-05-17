import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime

async def seed_data():
    mongo_uri = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
    db_name = "vjs_cms"
    
    client = AsyncIOMotorClient(mongo_uri)
    db = client[db_name]
    print(f"Connected to database: {db_name}")
    
    col = db["universal_content"]
    
    # 1. Delete existing awards under this page, subSection and category
    result = await col.delete_many({
        "mainPage": "About Us",
        "subSection": "Awards",
        "category": "Awards"
    })
    print(f"Deleted {result.deleted_count} old awards.")
    
    # 2. Define the 5 new awards according to specification
    awards = [
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "BNI Awards",
            "description": "Recognized for exceptional networking and business contribution at a national level.",
            "image": "/static/images/awards/bni.jpg",
            "image_url": "",
            "order": 1,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "ET NOW Awards",
            "description": "Honored by Economic Times NOW for outstanding leadership and industry impact.",
            "image": "/static/images/awards/etnow.jpg",
            "image_url": "",
            "order": 2,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "MSME Woman Led Startup",
            "description": "Awarded for building a thriving woman-led startup in the MSME sector.",
            "image": "/static/images/awards/msme.jpg",
            "image_url": "",
            "order": 3,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "Womenpreneur 2023",
            "description": "Celebrated as a leading woman entrepreneur driving change and innovation in 2023.",
            "image": "/static/images/awards/womenpreneur.jpg",
            "image_url": "",
            "order": 4,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "India Today Business Awards",
            "description": "Honored by India Today for exemplary business growth and vision.",
            "image": "/static/images/awards/indiatoday.jpg",
            "image_url": "",
            "order": 5,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
    ]
    
    # 3. Insert the 5 new awards
    for award in awards:
        await col.insert_one(award)
        print(f"Inserted New Award: {award['title']}")
        
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    asyncio.run(seed_data())
