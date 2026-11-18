# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(next=head)
        seek_ptr = head
        for _ in range(n):
            seek_ptr = seek_ptr.next
        write_ptr = dummy_head
        while seek_ptr:
            seek_ptr, write_ptr = seek_ptr.next, write_ptr.next
        write_ptr.next = write_ptr.next.next
        return dummy_head.next