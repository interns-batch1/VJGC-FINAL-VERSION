import sys
from pathlib import Path
from pymongo import MongoClient
from datetime import datetime

# Setup Paths
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "backend"))

# Use the exact MONGO_URI from env
MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["vjs_cms"]
col = db["universal_content"]

NOW = datetime.utcnow()

SEED_DATA = [
    {
        "mainPage": "About Us",
        "subSection": "About Group",
        "category": "Company Vision",
        "order": 1,
        "title": "COMPANY VISION",
        "description": "To be a world class leader in businesses that enrich lives and contribute to nations in building infrastructure through sustainable value creation.",
        "image": "/static/images/media/vision_landscape.png",
        "image_url": "/static/images/media/vision_landscape.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "About Group",
        "category": "Company Mission",
        "order": 2,
        "title": "COMPANY MISSION",
        "description": "Defining sustainable growth through innovative infrastructure, ethical trade, and financial excellence, empowering communities and nations for a resilient future.",
        "image": "/static/images/media/mission_industrial.png",
        "image_url": "/static/images/media/mission_industrial.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    }
]

print("Seeding Vision and Mission to database...")
for item in SEED_DATA:
    # Use filter keys to prevent duplicates
    filter_key = {
        "mainPage": item["mainPage"],
        "subSection": item["subSection"],
        "category": item["category"]
    }
    
    # Check if exists
    existing = col.find_one(filter_key)
    if existing:
        # Update without overwriting createdAt if it exists
        item.pop("createdAt", None)
        col.update_one(filter_key, {"$set": item})
        print(f"Updated category: {item['category']}")
    else:
        col.insert_one(item)
        print(f"Inserted category: {item['category']}")

print("Done seeding!")
client.close()
