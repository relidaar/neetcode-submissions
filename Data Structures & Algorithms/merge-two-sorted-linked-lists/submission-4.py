# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = ListNode(next=list1)
        list1 = result_head
        while list1.next and list2:
            if list2.val < list1.next.val:
                list2.next, list1.next, list2 = list1.next, list2, list2.next
            list1 = list1.next
        if list2:
            list1.next = list2
        return result_head.next 