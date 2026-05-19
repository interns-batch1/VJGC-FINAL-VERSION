from pymongo import MongoClient
import os

URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(URI)
db = client["vjs_cms"]
col = db["universal_content"]

print("--- Our Mission ---")
for doc in col.find({"category": "Our Mission"}):
    print(doc)

print("\n--- Our Vision ---")
for doc in col.find({"category": "Our Vision"}):
    print(doc)

client.close()
