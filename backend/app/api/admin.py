from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from app.schemas.achievement import Achievement, AchievementCreate
from app.schemas.about import About, AboutUpdate
from app.schemas.service import Service, ServiceCreate
from app.schemas.blog import Blog, BlogCreate
from app.core.config import settings
from typing import List
from datetime import datetime
import uuid
import os
import cloudinary
import cloudinary.uploader

# Configure Cloudinary
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME or "dmm9fvcox",
    api_key=settings.CLOUDINARY_API_KEY or "266587243377924",
    api_secret=settings.CLOUDINARY_API_SECRET or "Sh1eN-ObcD0AcH-ypg31IDGmCnM",
    secure=True
)

router = APIRouter()

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp", "gif", "mp4", "mov"}

# --- Media Management ---
@router.post("/media/upload")
async def upload_image(file: UploadFile = File(...), admin: str = Depends(get_current_admin)):
    try:
        file_ext = file.filename.split(".")[-1].lower()
        if file_ext not in ALLOWED_EXTENSIONS:
            raise HTTPException(status_code=400, detail=f"Invalid file type: {file_ext}")
        
        try:
            # Try Cloudinary upload first
            upload_result = cloudinary.uploader.upload(
                file.file,
                folder="vjs_group",
                resource_type="auto"
            )
            return {
                "url": upload_result["secure_url"],
                "filename": file.filename,
                "public_id": upload_result["public_id"]
            }
        except Exception as cloud_err:
            print(f"Cloudinary Upload failed: {str(cloud_err)}. Falling back to local upload.")
            
            # Local fallback saving
            import shutil
            import uuid
            
            # Setup path: vjs-website/static/images/media/uploads/
            PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
            SAVE_DIR = os.path.join(PROJECT_ROOT, "static", "images", "media", "uploads")
            os.makedirs(SAVE_DIR, exist_ok=True)
            
            # Generate unique filename to avoid duplicates
            unique_filename = f"{uuid.uuid4().hex}_{file.filename}"
            dest_path = os.path.join(SAVE_DIR, unique_filename)
            
            # Reset file pointer and write locally
            file.file.seek(0)
            with open(dest_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
                
            local_url = f"/static/images/media/uploads/{unique_filename}"
            print(f"Local fallback upload success! Saved to {dest_path}, URL: {local_url}")
            
            return {
                "url": local_url,
                "filename": file.filename,
                "public_id": f"local_{unique_filename}"
            }
            
    except Exception as e:
        print(f"Upload Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# --- About Us ---
@router.post("/about", response_model=About)
async def create_about(about: AboutUpdate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    update_data = {k: v for k, v in about.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    await db["about"].update_one({}, {"$set": update_data}, upsert=True)
    updated_about = await db["about"].find_one()
    if updated_about:
        updated_about["_id"] = str(updated_about["_id"])
    return updated_about

@router.put("/about", response_model=About)
async def update_about(about: AboutUpdate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    update_data = {k: v for k, v in about.model_dump().items() if v is not None}
    update_data["updated_at"] = datetime.utcnow()
    await db["about"].update_one({}, {"$set": update_data}, upsert=True)
    updated_about = await db["about"].find_one()
    updated_about["_id"] = str(updated_about["_id"])
    return updated_about

# --- Achievements ---
@router.post("/achievements", response_model=Achievement)
async def create_achievement(item: AchievementCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    doc["created_at"] = datetime.utcnow()
    result = await db["achievements"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/achievements/{id}")
async def delete_achievement(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    await db["achievements"].delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

@router.put("/achievements/{id}", response_model=Achievement)
async def update_achievement(id: str, item: AchievementCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    await db["achievements"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    doc = await db["achievements"].find_one({"_id": ObjectId(id)})
    doc["_id"] = str(doc["_id"])
    return doc

# --- Services ---
@router.post("/services", response_model=Service)
async def create_service(item: ServiceCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    result = await db["services"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/services/{id}")
async def delete_service(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    await db["services"].delete_one({"_id": ObjectId(id)})
    return {"message": "Deleted"}

@router.put("/services/{id}", response_model=Service)
async def update_service(id: str, item: ServiceCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    update_data = item.model_dump()
    await db["services"].update_one({"_id": ObjectId(id)}, {"$set": update_data})
    doc = await db["services"].find_one({"_id": ObjectId(id)})
    doc["_id"] = str(doc["_id"])
    return doc

# --- Blogs ---
@router.post("/news", response_model=Blog)
async def create_blog(item: BlogCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    doc = item.model_dump()
    doc["created_at"] = datetime.utcnow()
    result = await db["news"].insert_one(doc)
    doc["_id"] = str(result.inserted_id)
    return doc

@router.delete("/news/{id}")
async def delete_blog(id: str, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    oid = ObjectId(id)
    # Try deleting from news collection
    res1 = await db["news"].delete_one({"_id": oid})
    # Also try deleting from universal_content
    res2 = await db["universal_content"].delete_one({"_id": oid})
    
    if res1.deleted_count == 0 and res2.deleted_count == 0:
        raise HTTPException(status_code=404, detail="News item not found")
        
    return {"message": "Deleted"}

@router.put("/news/{id}", response_model=Blog)
async def update_blog(id: str, item: BlogCreate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from bson import ObjectId
    oid = ObjectId(id)
    update_data = item.model_dump()
    update_data["updated_at"] = datetime.utcnow()
    
    # Map 'status' back to 'isActive' for universal_content items
    is_active = update_data.get("status", "Published").lower() == "published"
    
    # Try updating in news collection
    res = await db["news"].update_one({"_id": oid}, {"$set": update_data})
    
    # Also try updating in universal_content
    uni_update = {
        "title": update_data.get("title"),
        "author": update_data.get("author"),
        "description": update_data.get("summary") or update_data.get("content"),
        "image": update_data.get("image_url"),
        "isActive": is_active,
        "updatedAt": datetime.utcnow()
    }
    await db["universal_content"].update_one({"_id": oid}, {"$set": uni_update})
    
    doc = await db["news"].find_one({"_id": oid}) or await db["universal_content"].find_one({"_id": oid})
    if not doc:
        raise HTTPException(status_code=404, detail="News item not found")
        
    doc["_id"] = str(doc["_id"])
    return doc

@router.get("/news", response_model=List[Blog])
async def list_admin_news(db = Depends(get_database)):
    from app.api.public import list_news
    return await list_news(db)

# --- Admin Profile & Security Settings ---
from pydantic import BaseModel

class ProfileUpdate(BaseModel):
    name: str
    email: str
    avatar: str

class PasswordChange(BaseModel):
    current_password: str
    new_password: str

@router.get("/me")
async def get_my_profile(db = Depends(get_database), admin: str = Depends(get_current_admin)):
    profile = await db["admin_profile"].find_one({"username": admin})
    if not profile:
        profile = await db["admin_profile"].find_one({"email": admin})
        
    if not profile:
        return {
            "name": "Admin",
            "email": "admin@vjsgroups.com" if admin == "admin" else admin,
            "avatar": "/static/images/media/avatar.png"
        }
    
    return {
        "name": profile.get("name", "Admin"),
        "email": profile.get("email", admin),
        "avatar": profile.get("avatar") or "/static/images/media/avatar.png"
    }

@router.put("/profile")
async def update_my_profile(profile_data: ProfileUpdate, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    await db["admin_profile"].update_one(
        {"username": admin},
        {
            "$set": {
                "name": profile_data.name,
                "email": profile_data.email,
                "avatar": profile_data.avatar,
                "updatedAt": datetime.utcnow()
            }
        },
        upsert=True
    )
    return {"message": "Profile updated successfully"}

@router.put("/change-password")
async def change_admin_password(pw_data: PasswordChange, db = Depends(get_database), admin: str = Depends(get_current_admin)):
    from app.core import security
    
    # 1. Fetch current password hash
    profile = await db["admin_profile"].find_one({"username": admin})
    
    if profile and "password_hash" in profile:
        current_hash = profile["password_hash"]
    else:
        # Fallback to default password
        from app.api.auth import ADMIN_PASSWORD_HASH
        current_hash = ADMIN_PASSWORD_HASH
        
    # 2. Verify current password
    if not security.verify_password(pw_data.current_password, current_hash):
        raise HTTPException(status_code=400, detail="Incorrect current password")
        
    # 3. Hash and save new password
    new_hash = security.get_password_hash(pw_data.new_password)
    await db["admin_profile"].update_one(
        {"username": admin},
        {
            "$set": {
                "password_hash": new_hash,
                "updatedAt": datetime.utcnow()
            }
        },
        upsert=True
    )
    return {"message": "Password changed successfully"}
