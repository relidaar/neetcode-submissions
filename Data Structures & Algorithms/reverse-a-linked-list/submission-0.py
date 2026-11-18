# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prevNode, currentNode = None, head
        while currentNode:
            currentNode.next, prevNode, currentNode = prevNode, currentNode, currentNode.next
        return prevNode