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

# Delete old Foundation data to ensure clean seeding
col.delete_many({"mainPage": "About Us", "subSection": "Foundation"})

NOW = datetime.utcnow()

SEED_DATA = [
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Hero Section",
        "order": 1,
        "title": "Empowering Communities, Transforming Lives",
        "description": "At Vijayalakshmi Foundation, we are committed to driving grassroots change through sustainable education, healthcare, and environmental initiatives. Together, we build a future where every individual has the opportunity to thrive.",
        "image": "/static/images/media/foundation_edu.png",
        "image_url": "/static/images/media/foundation_edu.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Purpose Statement",
        "order": 2,
        "title": "Purpose Statement",
        "description": "Driving community upliftment and sustainable social impact through education, basic support, and local development.",
        "image": "/static/images/media/foundation_visit_bg.png",
        "image_url": "/static/images/media/foundation_visit_bg.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Aditya IT Academy",
        "order": 3,
        "title": "Where Education Meets Opportunity",
        "description": "Aditya Institute - Academy & IT Skilling Hub, powered by the Vijayalakshmi Foundation, is built to transform learning into real careers. We are part of a larger mission to empower students through education, skill development, and employment opportunities.",
        "image": "/static/images/media/aditya_institute_learning.png",
        "image_url": "/static/images/media/aditya_institute_learning.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Vijay Anjaneya CSR",
        "order": 4,
        "title": "Vijay Anjaneya Traders - Sharing Nourishment with Humanity",
        "description": "Vijay Anjaneya Traders actively supports orphanages and old age homes by providing food, fruits, and essential supplies to those in need. We believe that no individual should experience hunger or neglect.",
        "image": "/static/images/media/hero_foundation_2.png",
        "image_url": "/static/images/media/hero_foundation_2.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Aditya Powers",
        "order": 5,
        "title": "Aditya Powers – Empowering Lives Through Sustainable Energy",
        "description": "Aditya Powers proudly supports recently widowed women by providing free solar energy solutions for their homes. This initiative is designed to reduce financial burden while promoting sustainable and independent living.",
        "image": "/static/images/media/vjs_energy_glance_1.png",
        "image_url": "/static/images/media/vjs_energy_glance_1.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Springreen",
        "order": 6,
        "title": "Springreen – Creating Opportunities for Better Futures",
        "description": "Springreen is dedicated to empowering unemployed youth, bachelors, and economically disadvantaged individuals by creating meaningful employment opportunities. We believe that employment is not just a source of income but a pathway to dignity, confidence, and self-reliance.",
        "image": "/static/images/media/whyus_training.png",
        "image_url": "/static/images/media/whyus_training.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Real Estate Division",
        "order": 7,
        "title": "Real Estate Division – Profits with a Purpose",
        "description": "Our Real Estate Division proudly contributes 1% of its profits toward supporting old age homes and elderly care initiatives. We strongly believe that business growth should also create social value and meaningful community impact.",
        "image": "/static/images/media/hero_foundation_1.png",
        "image_url": "/static/images/media/hero_foundation_1.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "Aham Grham",
        "order": 8,
        "title": "Aham Grham – Wellness with a Social Purpose",
        "description": "Aham Grham organizes yoga camps and wellness programs focused on promoting healthy living, inner peace, and mental wellbeing. As part of our social contribution, a portion of the proceeds from these initiatives supports orphanages and children in need.",
        "image": "/static/images/media/vjs_yoga_new.png",
        "image_url": "/static/images/media/vjs_yoga_new.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "At a Glance",
        "order": 1,
        "title": "Education Support",
        "description": "Assistance for students, learning resources, and basic digital exposure to build future-ready talent.",
        "image": "/static/images/media/glance_empowerment.png",
        "image_url": "/static/images/media/glance_empowerment.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "At a Glance",
        "order": 2,
        "title": "Social Service",
        "description": "Financial and material support during critical needs, rural assistance, and emergency support programs.",
        "image": "/static/images/media/glance_healthcare.png",
        "image_url": "/static/images/media/glance_healthcare.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    },
    {
        "mainPage": "About Us",
        "subSection": "Foundation",
        "category": "At a Glance",
        "order": 3,
        "title": "Community Development",
        "description": "Driving sustainable grassroots development through local engagement and infrastructure needs.",
        "image": "/static/images/media/glance_environment.png",
        "image_url": "/static/images/media/glance_environment.png",
        "isActive": True,
        "updatedAt": NOW,
        "createdAt": NOW
    }
]

print("Seeding Foundation items to database with correct production images...")
for item in SEED_DATA:
    col.insert_one(item)
    print(f"Inserted category: {item['category']}")

print("Done seeding Foundation!")
client.close()
