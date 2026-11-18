# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sourceListHead, listToMerge = ListNode(next=list1), list2
        sourceList = sourceListHead
        while sourceList.next and listToMerge:
            if listToMerge.val < sourceList.next.val:
                listToMerge.next, sourceList.next, listToMerge = sourceList.next, listToMerge, listToMerge.next
            sourceList = sourceList.next

        if listToMerge:
            sourceList.next = listToMerge

        return sourceListHead.next