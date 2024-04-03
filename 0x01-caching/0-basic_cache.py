#!/usr/bin/env python3
"""0-basic_cache.py
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """Adds an item incache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Sorts out an item by key.
        """
        return self.cache_data.get(key, None)
