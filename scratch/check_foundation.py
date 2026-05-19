import pymongo
import os

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = pymongo.MongoClient(MONGO_URI)
db = client["vjs_cms"]
col = db["universal_content"]

print("--- FOUNDATION ITEMS IN DB ---")
query = {"mainPage": "About Us", "subSection": "Foundation"}
for doc in col.find(query).sort("order", 1):
    print(f"ID: {doc.get('_id')}")
    print(f"  Category: {doc.get('category')}")
    print(f"  Title: {doc.get('title')}")
    print(f"  Image: {doc.get('image')}")
    print(f"  Image URL: {doc.get('image_url')}")
    print(f"  isActive: {doc.get('isActive')}")
    print("-" * 40)

client.close()
