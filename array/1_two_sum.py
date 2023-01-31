'''
https://leetcode.com/problems/two-sum/
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests

class Solution(object):
    def twoSum(self, nums, target):
        pairs = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in pairs:
                return [i, pairs[pair]]
            pairs[num] = i
