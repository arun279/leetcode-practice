'''
https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution
class Solution(object):
    def reverseList(self, head):
        prev = None 
        curr = head
        while curr is not None:
            next_temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = next_temp
        return prev
        
    def reverseListRecursive(self, head,  prev=None):
        if not head:
            return prev
        next_temp = head.next 
        head.next = prev
        return self.reverseListRecursive(next_temp, head)


# s = Solution()
# test_cases = [
#     ([1,2,3,4,5], [5,4,3,2,1]),
#     ([1,2], [2,1]),
#     ([], []),
# ]
# for i, (inputs, expected_output) in enumerate(test_cases):
#     head = None
#     curr = None
#     for val in inputs:
#         if not head:
#             head = ListNode(val)
#             curr = head
#         else:
#             curr.next = ListNode(val)
#             curr = curr.next

#     reversed_head = s.reverseList(head)
#     result = []
#     while reversed_head:
#         result.append(reversed_head.val)
#         reversed_head = reversed_head.next
#     if result == expected_output:
#         print(f"Test case {i + 1}: PASSED")
#     else:
#         print(f"Test case {i + 1}: FAILED")
#         print(f"Inputs: {inputs}")
#         print(f"Output: {result}")
#         print(f"Expected Output: {expected_output}")

