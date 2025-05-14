#!/usr/bin/env python3
""" LIFO Cache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ A LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache (LIFO logic) """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last = self.stack.pop()
                del self.cache_data[last]
                print("DISCARD:", last)
            self.stack.append(key)
        else:
            self.stack.remove(key)
            self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
