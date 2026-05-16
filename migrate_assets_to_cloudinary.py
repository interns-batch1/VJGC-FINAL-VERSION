import os
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import cloudinary
import cloudinary.uploader
from bson import ObjectId

# Cloudinary Config (Same as in .env)
CLOUD_NAME = "dmm9fvcox"
API_KEY = "266587243377924"
API_SECRET = "Sh1eN-ObcD0AcH-ypg31IDGmCnM"

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

# MongoDB Config
MONGO_URI = "mongodb+srv://Admin:Vjgc-spring@cluster0.euw17oq.mongodb.net/?appName=Cluster0"
DATABASE_NAME = "vjs_cms"

# Base directory for local files
BASE_DIR = os.getcwd()

async def migrate_assets():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DATABASE_NAME]
    
    # Collections to check
    collections = ["universal_content", "news", "achievements", "services"]
    
    total_migrated = 0
    
    for coll_name in collections:
        print(f"\nScanning collection: {coll_name}")
        cursor = db[coll_name].find({})
        
        async for doc in cursor:
            updated_fields = {}
            
            # Check common image fields
            for field in ["image", "image_url", "video_url"]:
                if field in doc and doc[field]:
                    url = doc[field]
                    
                    # If it's a local path
                    if url.startswith("/static/") or url.startswith("/uploads/") or url.startswith("http://localhost"):
                        
                        # Resolve local path
                        local_path = ""
                        if url.startswith("/static/"):
                            local_path = os.path.join(BASE_DIR, url.lstrip("/"))
                        elif url.startswith("/uploads/"):
                            local_path = os.path.join(BASE_DIR, url.lstrip("/"))
                        elif "localhost:5000/uploads/" in url:
                            filename = url.split("/")[-1]
                            local_path = os.path.join(BASE_DIR, "uploads", filename)
                            
                        if local_path and os.path.exists(local_path):
                            print(f"  Uploading {url} ...")
                            try:
                                # Determine folder based on collection
                                folder = f"vjs_group/{coll_name}"
                                
                                upload_result = cloudinary.uploader.upload(
                                    local_path,
                                    folder=folder,
                                    resource_type="auto"
                                )
                                
                                new_url = upload_result["secure_url"]
                                updated_fields[field] = new_url
                                print(f"    Success: {new_url}")
                                total_migrated += 1
                            except Exception as e:
                                print(f"    Error uploading {local_path}: {e}")
                        else:
                            print(f"    File not found: {local_path}")
            
            if updated_fields:
                await db[coll_name].update_one({"_id": doc["_id"]}, {"$set": updated_fields})
                
    print(f"\nMigration complete! Total assets migrated: {total_migrated}")
    client.close()

if __name__ == "__main__":
    asyncio.run(migrate_assets())
