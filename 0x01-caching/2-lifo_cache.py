#!/usr/bin/env python3
"""Import modules for LIFOCache class."""

from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    Class is a last-in-first-out caching system
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
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Returns the value in the dictionary linked to the key."""
        return (self.cache_data.get(key, None))
