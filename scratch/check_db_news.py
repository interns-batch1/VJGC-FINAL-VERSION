import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
# Explicitly use vjs_cms
db = client["vjs_cms"]

print(f"Connected to DB: {db.name}")

col = db["universal_content"]
print("--- INSIGHTS NEWS ITEMS ---")
# Category might be different, let's search all or filter by what we saw in main.py
for doc in col.find({"category": {"$in": ["Insights News", "Latest_News", "News", "Insights / News", "News Section"]}}):
    print(f"ID: {doc.get('_id')}")
    print(f"Title: {doc.get('title')}")
    print(f"Image: {doc.get('image')}")
    print(f"ImageURL: {doc.get('image_url')}")
    print("-" * 20)

client.close()
