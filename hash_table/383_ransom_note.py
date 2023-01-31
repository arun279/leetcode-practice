'''
https://leetcode.com/problems/ransom-note/
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests
from collections import Counter

class Solution(object):
    def canConstruct_count(self, ransomNote, magazine):
        # this works faster on leetcode using less memory, but the folder is meant for hashtable learning, so the method below uses that
        for s in set(ransomNote):
            if ransomNote.count(s) > magazine.count(s):
                return False
        return True

    def canConstruct(self, ransomNote, magazine):
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        
        for char in ransomNote_counter:
            if ransomNote_counter[char] > magazine_counter[char]:
                return False
        
        return True

# solution = Solution()
# test_cases = [
#     (["a", "b"], False),
#     (["aa", "ab"], False),
#     (["aa", "aab"], True),
# ]
# run_tests.run_tests(solution.canConstruct, test_cases)
