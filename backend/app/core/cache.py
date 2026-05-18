from typing import Dict, Any

class CMSCache:
    def __init__(self):
        # In-memory dictionary to store page contexts
        self._cache: Dict[str, Any] = {}

    def get(self, key: str) -> Any:
        return self._cache.get(key)

    def set(self, key: str, value: Any):
        self._cache[key] = value

    def clear(self):
        print("DEBUG CACHE: In-memory CMS cache invalidated and cleared.")
        self._cache.clear()

cms_cache = CMSCache()
