import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["vjs_cms"]
col = db["universal_content"]

print("--- UPDATING NEWS VIDEO PATHS ---")

count = 0
for doc in col.find():
    updates = {}
    
    # Check image field
    img = doc.get("image")
    if img and "news video" in img:
        new_img = img.replace("news video", "news_video")
        updates["image"] = new_img
        print(f"Updating image: {img} -> {new_img}")
        
    # Check image_url field
    img_url = doc.get("image_url")
    if img_url and "news video" in img_url:
        new_img_url = img_url.replace("news video", "news_video")
        updates["image_url"] = new_img_url
        print(f"Updating image_url: {img_url} -> {new_img_url}")

    if updates:
        col.update_one({"_id": doc["_id"]}, {"$set": updates})
        count += 1

print(f"Updated {count} documents.")
client.close()
