import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums) # length of array
        positives = set() # initialize empty set to hold only positives
        for i in range(n): # iterate through nums
            if nums[i] > 0:
                positives.add(nums[i]) # add only +ve items to positives
        for i in range(1,n+1): # iterate through 1 to n+1, n+1 being theoretically the largest possible solution
            if i not in positives:
                return i # smallest that's not there is the answer
        return n + 1 # return theoretical max
