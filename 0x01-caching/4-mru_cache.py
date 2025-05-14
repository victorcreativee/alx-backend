#!/usr/bin/env python3
""" MRU Cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ A MRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """ Add an item in the cache (MRU logic) """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = self.usage_order.pop()
            del self.cache_data[mru]
            print("DISCARD:", mru)

        self.cache_data[key] = item
        self.usage_order.append(key)

    def get(self, key):
        """ Get an item by key and update usage """
        if key in self.cache_data:
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
