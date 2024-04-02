#!/usr/bin/env python3
"""Import from BaseCaching class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class is a caching system that inherits
    from BaseCaching class.
    """
    def put(self, key, item):
        """Assigns the item value for the key."""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in the dictionary linked to the key."""
        return (self.cache_data.get(key, None))
