import os
from pathlib import Path

# Simulate main.py BASE_DIR calculation
MAIN_PY_PATH = Path(r"c:\Users\Admin\vjgc-final\vjs-website\backend\app\main.py")
BASE_DIR = MAIN_PY_PATH.resolve().parent.parent.parent
STATIC_DIR = BASE_DIR / "static"
VIDEO_PATH = STATIC_DIR / "images" / "news_video" / "Code.mp4"

print(f"BASE_DIR: {BASE_DIR}")
print(f"STATIC_DIR: {STATIC_DIR}")
print(f"STATIC_DIR exists: {STATIC_DIR.exists()}")
print(f"VIDEO_PATH: {VIDEO_PATH}")
print(f"VIDEO_PATH exists: {VIDEO_PATH.exists()}")

# List static dir
if STATIC_DIR.exists():
    print("Files in static/images:")
    try:
        print(os.listdir(STATIC_DIR / "images"))
    except:
        print("Could not list images dir")
