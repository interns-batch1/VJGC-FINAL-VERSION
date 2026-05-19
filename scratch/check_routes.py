import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from app.main import app

print("--- REGISTERED FASTAPI ROUTES ---")
for route in app.routes:
    methods = getattr(route, "methods", None)
    print(f"Path: {route.path} | Methods: {methods} | Name: {route.name}")
