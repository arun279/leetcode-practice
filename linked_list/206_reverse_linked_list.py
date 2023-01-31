'''
https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
