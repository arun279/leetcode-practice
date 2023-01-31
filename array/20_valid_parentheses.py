'''
https://leetcode.com/problems/valid-parentheses/
'''
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
