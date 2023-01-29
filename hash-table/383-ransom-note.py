'''
https://leetcode.com/problems/ransom-note/
'''
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

solution = Solution()
print(solution.canConstruct("a", "b")) # False
print(solution.canConstruct("aa", "ab")) # False
print(solution.canConstruct("aa", "aab")) # True
