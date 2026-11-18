# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        write, read = dummy, dummy
        while n > 0:
            read = read.next
            n -= 1
        while read.next:
            read = read.next
            write = write.next
        write.next = write.next.next
        return dummy.next
        