#!/usr/bin/env python3
"""Import modules for FIFOCache class"""

from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Class is a first-in-first-out caching system
    that inherits from the BaseCaching class
    """
    def __init__(self):
        """Initialises cache class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns the item value for the key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Returns the value in the dictionary linked to the key."""
        return (self.cache_data.get(key, None))
