import sys
# Trigger fresh optimized build v2
from pathlib import Path

# Add the project root and backend directory to sys.path
# This helps both Vercel and IDEs find the 'app' module
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "backend"))

# Now we can import the FastAPI app
try:
    from app.main import app
except ImportError:
    # Fallback for different environments
    from backend.app.main import app

# Vercel looks for 'app'
app = app
