'''
https://leetcode.com/problems/two-sum/
'''
class Solution(object):
    def twoSum(self, nums, target):
        pairs = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in pairs:
                return [i, pairs[pair]]
            pairs[num] = i