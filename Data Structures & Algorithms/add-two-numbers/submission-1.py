# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getNext(node):
    return node.next if node else None

def getValue(node):
    return node.val if node else 0

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(next=l1)
        result, remainder = result_head, 0
        while l1 or l2 or remainder > 0:
            sum_result = getValue(l1) + getValue(l2) + remainder
            result.next, remainder = ListNode(val=sum_result % 10), sum_result // 10
            l1, l2, result = getNext(l1), getNext(l2), result.next
        return result_head.next