import sys
import uvicorn
from pathlib import Path

# Add the project root and backend directory to sys.path
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "backend"))

if __name__ == "__main__":
    try:
        from app.main import app
    except ImportError:
        from backend.app.main import app
        
    # Use string import and reload=True so changes take effect immediately
    uvicorn.run("backend.app.main:app" if "backend" in sys.modules else "app.main:app", host="127.0.0.1", port=5005, reload=True)
