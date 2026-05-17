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
    
    # 1. Advisor Coordinators (category="Advisors")
    advisors = [
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Advisors",
            "title": "Zubayer Hasan",
            "description": "Strategy Lead",
            "image": "/static/images/media/img_27.jpg",
            "image_url": "",
            "order": 1,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Advisors",
            "title": "Maria Escolova",
            "description": "Operations Head",
            "image": "/static/images/media/img_28.jpg",
            "image_url": "",
            "order": 2,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Advisors",
            "title": "Rashedul Kabir",
            "description": "Finance Director",
            "image": "/static/images/media/img_29.jpg",
            "image_url": "",
            "order": 3,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        },
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Advisors",
            "title": "Cristiano Messi",
            "description": "Supply Chain",
            "image": "/static/images/media/img_30.jpg",
            "image_url": "",
            "order": 4,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
    ]
    
    # 2. Global Recognition (category="Awards")
    awards = [
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": "Excellence 2024",
            "description": "Highest industry safety and quality standards recognition.",
            "image": "",
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
            "title": "Innovation Award",
            "description": "Breakthrough solutions in green energy and utilities.",
            "image": "",
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
            "title": "Sustainability Lead",
            "description": "Commemorated for sustainable supply chain practices.",
            "image": "",
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
            "title": "Leadership Gold",
            "description": "Recognized for outstanding corporate governance.",
            "image": "",
            "image_url": "",
            "order": 4,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
    ]
    
    # 3. Our Success Story (category="Success Story")
    story = [
        {
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Success Story",
            "title": "Our Success Story",
            "description": "From a local enterprise to a diversified global group, our journey has been defined by resilience, innovation, and long-term value creation for our stakeholders.",
            "image": "/static/images/media/img_12.jpg",
            "image_url": "",
            "order": 1,
            "isActive": True,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow()
        }
    ]
    
    # Check and insert Advisors
    for advisor in advisors:
        exists = await col.find_one({
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Advisors",
            "title": advisor["title"]
        })
        if not exists:
            await col.insert_one(advisor)
            print(f"Inserted Advisor: {advisor['title']}")
        else:
            print(f"Advisor already exists: {advisor['title']}")
            
    # Check and insert Awards
    for award in awards:
        exists = await col.find_one({
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Awards",
            "title": award["title"]
        })
        if not exists:
            await col.insert_one(award)
            print(f"Inserted Award: {award['title']}")
        else:
            print(f"Award already exists: {award['title']}")
            
    # Check and insert Success Story
    for s in story:
        exists = await col.find_one({
            "mainPage": "About Us",
            "subSection": "Awards",
            "category": "Success Story",
            "title": s["title"]
        })
        if not exists:
            await col.insert_one(s)
            print(f"Inserted Success Story: {s['title']}")
        else:
            print(f"Success Story already exists: {s['title']}")

if __name__ == "__main__":
    asyncio.run(seed_data())
