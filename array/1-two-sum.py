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

s = Solution()

# Example 1
nums = [2, 7, 11, 15]
target = 9
assert set(s.twoSum(nums, target)) == {0, 1}

# Example 2
nums = [3, 2, 4]
target = 6
assert set(s.twoSum(nums, target)) == {1, 2}

# Example 3
nums = [3, 3]
target = 6
assert set(s.twoSum(nums, target)) == {0, 1}