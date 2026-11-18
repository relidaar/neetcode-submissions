# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result, remainder, prev = l1, 0, None
        while l1 and l2:
            l1.val += l2.val + remainder
            l1.val, remainder = l1.val % 10, l1.val // 10
            l1, l2, prev = l1.next, l2.next, l1
        l1 = l1 if l1 else l2
        prev.next = l1
        while l1:
            l1.val += remainder
            l1.val, remainder = l1.val % 10, l1.val // 10
            l1, prev = l1.next, l1
        if remainder > 0:
            prev.next = ListNode(val=remainder)
        return result