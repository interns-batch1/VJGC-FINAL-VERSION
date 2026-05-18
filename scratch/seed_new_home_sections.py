from pymongo import MongoClient
from datetime import datetime

URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(URI)
db = client["vjs_cms"]
col = db["universal_content"]

NOW = datetime.utcnow()

SEED_DATA = [
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Mission",
        "title": "Our Mission",
        "description": "To deliver innovative and reliable solutions across diverse industries by combining technology, expertise, and customer-focused services—empowering businesses and communities to achieve sustainable growth.",
        "image": "/static/images/icon/icon_10.svg",
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Vision",
        "title": "Our Vision",
        "description": "To become a trusted and leading group of companies recognized for excellence in technology, education, wellness, and global trade, creating long-term value and positive impact worldwide.",
        "image": "/static/images/icon/icon_11.svg",
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Leadership Statement",
        "title": "Ms. M. Vijayalakshmi",
        "description": "Empowerment is not just about providing technology or services; it's about building an ecosystem where innovation and trust create a legacy of sustainable growth for everyone.",
        "image": "/static/images/media/chairman_portrait.png",
        "cta_text": "Managing Director of VJS Group",
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Purpose",
        "title": "Sustainability",
        "description": "Driving environmental impact through global reforestation initiatives.",
        "image": "/static/images/media/csr_sustainability.png",
        "order": 0,
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Purpose",
        "title": "Solutions",
        "description": "Empowering businesses with full-stack digital transformation.",
        "image": "/static/images/media/csr_solutions.png",
        "order": 1,
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Purpose",
        "title": "Education",
        "description": "Providing skills and education for a digital-first future.",
        "image": "/static/images/media/csr_education.png",
        "order": 2,
        "isActive": True,
        "updatedAt": NOW
    },
    {
        "mainPage": "home",
        "subSection": "",
        "category": "Our Purpose",
        "title": "Wellness",
        "description": "Fostering physical and mental balance through ancient wisdom.",
        "image": "/static/images/media/csr_wellness.png",
        "order": 3,
        "isActive": True,
        "updatedAt": NOW
    }
]

for item in SEED_DATA:
    # Only insert if they do not exist to prevent duplicate creation
    existing = col.find_one({
        "mainPage": item["mainPage"],
        "category": item["category"],
        "title": item["title"]
    })
    if not existing:
        col.insert_one(item)
        print(f"Seeded: {item['category']} - {item['title']}")
    else:
        print(f"Skipped (already exists): {item['category']} - {item['title']}")

client.close()
print("Seeding complete.")
