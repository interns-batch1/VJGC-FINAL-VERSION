from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.core import security
from app.core.config import settings
from app.db.mongodb import get_database

router = APIRouter()

# Simple hardcoded admin for demonstration
# In production, you would fetch this from MongoDB
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = security.get_password_hash("vjs_admin_123") 

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db = Depends(get_database)):
    """
    Login endpoint to get JWT access token.
    Accepts 'username' and 'password' as form-data.
    """
    username = form_data.username
    password = form_data.password
    
    # 1. Try finding in the database admin_profile
    profile = await db["admin_profile"].find_one({
        "$or": [
            {"username": username},
            {"email": username}
        ]
    })
    
    is_valid = False
    if profile:
        stored_hash = profile.get("password_hash")
        if stored_hash:
            is_valid = security.verify_password(password, stored_hash)
            subject_username = profile.get("username") or username
        else:
            is_valid = security.verify_password(password, ADMIN_PASSWORD_HASH)
            subject_username = username
    else:
        # Fallback to hardcoded admin credentials
        if username in [ADMIN_USERNAME, "admin@vjsgroups.com"]:
            is_valid = security.verify_password(password, ADMIN_PASSWORD_HASH)
            subject_username = username
        else:
            is_valid = False
            subject_username = username
            
    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(subject=subject_username)
    return {"access_token": access_token, "token_type": "bearer"}
