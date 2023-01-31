'''
https://leetcode.com/problems/lru-cache/
'''
class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.access_list = []
        
    def get(self, key):
        if key in self.cache:
            self.access_list.remove(key)
            self.access_list.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.access_list.remove(key)
        elif len(self.cache) == self.capacity:
            del self.cache[self.access_list[0]]
            self.access_list.pop(0)
        self.cache[key] = value
        self.access_list.append(key)