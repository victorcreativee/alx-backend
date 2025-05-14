#!/usr/bin/env python3
""" LRU Cache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ A LRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache (LRU logic) """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = self.usage_order.pop(0)
            del self.cache_data[lru]
            print("DISCARD:", lru)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key and update usage """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
