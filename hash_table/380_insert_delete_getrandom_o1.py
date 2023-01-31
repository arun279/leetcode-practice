'''
https://leetcode.com/problems/insert-delete-getrandom-o1/
'''
import random

class RandomizedSet(object):
    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val):
        if val in self.dict:
            return False
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val):
        if val not in self.dict:
            return False
        idx, last = self.dict[val], self.list[-1]
        self.list[idx], self.dict[last] = last, idx
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self):
        return self.list[random.randint(0, len(self.list) - 1)]
