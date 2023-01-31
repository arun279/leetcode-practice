import random
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests

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


# obj = RandomizedSet()

# print(obj.insert(1)) # True
# print(obj.remove(2)) # False
# print(obj.insert(2)) # True
# print(obj.getRandom()) # 1 or 2
# print(obj.remove(1)) # True
# print(obj.insert(2)) # False
# print(obj.getRandom()) # 2