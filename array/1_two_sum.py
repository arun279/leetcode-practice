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

# s = Solution()
# test_cases = [
#     ([[2, 7, 11, 15], 9], [1, 0]),
#     ([[3, 2, 4], 6], [2, 1]),
#     ([[3, 3], 6], [1, 1]),
# ]
# run_tests.run_tests(s.twoSum, test_cases)
