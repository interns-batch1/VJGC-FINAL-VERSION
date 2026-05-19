from pymongo import MongoClient
import os
import sys

# Add backend to python path to import app config if needed, or do it directly
URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(URI)
db = client["vjs_cms"]
col = db["universal_content"]

new_desc = "To deliver innovative and reliable solutions through technology, expertise, and customer-focused services, empowering business to achieve sustainable growth"

res = col.update_one(
    {"category": "Our Mission", "mainPage": "home"},
    {"$set": {"description": new_desc}}
)

print(f"Matched count: {res.matched_count}")
print(f"Modified count: {res.modified_count}")

# Print updated document
doc = col.find_one({"category": "Our Mission", "mainPage": "home"})
print("Updated document:")
print(doc)

client.close()
