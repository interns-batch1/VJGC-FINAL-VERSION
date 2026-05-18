from pymongo import MongoClient

MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client["vjs_cms"]
col = db["universal_content"]

print("Listing all documents in universal_content:")
for doc in col.find():
    print(f"ID: {doc.get('_id')}, mainPage: {doc.get('mainPage')}, subSection: {doc.get('subSection')}, category: {doc.get('category')}, title: {doc.get('title')}, image: {doc.get('image')}, image_url: {doc.get('image_url')}")

client.close()
