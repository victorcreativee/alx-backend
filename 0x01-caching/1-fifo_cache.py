#!/usr/bin/env python3
""" FIFO Cache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ A FIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache (FIFO logic) """
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest = self.queue.pop(0)
                del self.cache_data[oldest]
                print("DISCARD:", oldest)
            self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
