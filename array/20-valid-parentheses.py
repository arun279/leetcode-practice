'''
https://leetcode.com/problems/valid-parentheses/
'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from run_tests import run_tests

class Solution(object):
    def isValid(self, s):
        stack = []
        for item in s:
            if item == '{' or item == '(' or item == '[':
                stack.append(item)
            else:
                if not stack:
                    return False
                if item == '}' and stack[-1] == "{":
                    stack.pop()
                elif item == ']' and stack[-1] == "[":
                    stack.pop()
                elif item == ')' and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return not stack
        
s = Solution()
test_cases = [
    (["()"], True),
    (["()[]{}"], True),
    (["(]"], False),
]
run_tests.run_tests(s.isValid, test_cases)
