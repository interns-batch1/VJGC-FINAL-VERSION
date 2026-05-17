from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.core.config import settings
from app.db.mongodb import get_database
from app.api.deps import get_current_admin
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

# Schema for profile updates
class ProfileUpdate(BaseModel):
    name: str
    email: str
    avatar: Optional[str] = None

# Schema for password updates
class PasswordChange(BaseModel):
    current_password: str
    new_password: str

async def init_admin_in_db(db):
    """
    Ensure at least one admin document exists in MongoDB.
    """
    admin_doc = await db["admins"].find_one({"username": "admin"})
    if not admin_doc:
        await db["admins"].insert_one({
            "username": "admin",
            "name": "Admin User",
            "email": "admin@vjsgroups.com",
            "avatar": "/avatars/shadcn.jpg",
            "password_hash": security.get_password_hash("vjs_admin_123")
        })

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_database)):
    """
    Login endpoint to get JWT access token.
    Accepts 'username' and 'password' as form-data.
    """
    await init_admin_in_db(db)
    admin_doc = await db["admins"].find_one({"username": form_data.username})
    
    if not admin_doc or not security.verify_password(form_data.password, admin_doc["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(subject=admin_doc["username"])
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def get_profile(db = Depends(get_database), username: str = Depends(get_current_admin)):
    """
    Get the current logged-in admin user's profile details.
    """
    await init_admin_in_db(db)
    admin_doc = await db["admins"].find_one({"username": username})
    if not admin_doc:
        raise HTTPException(status_code=404, detail="Admin not found")
    
    return {
        "username": admin_doc["username"],
        "name": admin_doc.get("name", "Admin User"),
        "email": admin_doc.get("email", "admin@vjsgroups.com"),
        "avatar": admin_doc.get("avatar", "/avatars/shadcn.jpg")
    }

@router.put("/profile")
async def update_profile(
    profile_data: ProfileUpdate,
    db = Depends(get_database),
    username: str = Depends(get_current_admin)
):
    """
    Update the admin name, email, and avatar in MongoDB.
    """
    await init_admin_in_db(db)
    result = await db["admins"].update_one(
        {"username": username},
        {"$set": {
            "name": profile_data.name,
            "email": profile_data.email,
            "avatar": profile_data.avatar
        }}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Admin not found")
        
    return {"message": "Profile updated successfully"}

@router.put("/change-password")
async def change_password(
    password_data: PasswordChange,
    db = Depends(get_database),
    username: str = Depends(get_current_admin)
):
    """
    Update the admin password in MongoDB.
    """
    await init_admin_in_db(db)
    admin_doc = await db["admins"].find_one({"username": username})
    if not admin_doc:
        raise HTTPException(status_code=404, detail="Admin not found")
        
    # Verify current password
    if not security.verify_password(password_data.current_password, admin_doc["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect current password"
        )
        
    # Hash new password and update
    new_hash = security.get_password_hash(password_data.new_password)
    await db["admins"].update_one(
        {"username": username},
        {"$set": {"password_hash": new_hash}}
    )
    
    return {"message": "Password changed successfully"}
