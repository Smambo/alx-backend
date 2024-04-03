#!/usr/bin/env python3
"""Import modules for MRUCache class"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    Class is a most-recently-used caching system
    that inherits from the BaseCaching class
    """
    def __init__(self):
        """Initialises cache class."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Assigns the item value for the key"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in the dictionary linked to the key"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return (self.cache_data.get(key, None))
