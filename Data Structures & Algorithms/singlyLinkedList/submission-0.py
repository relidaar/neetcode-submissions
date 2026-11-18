class LinkedListNode:
    def __init__(self, next=None, value=None):
        self.next = next
        self.value = value

class LinkedList:
    
    def __init__(self):
        self.head = LinkedListNode()
        self.size = 0
    
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head.next
        while index > 0:
            current = current.next
            index -= 1
        return current.value

    def insertHead(self, val: int) -> None:
        self.head.next = LinkedListNode(self.head.next, val)
        self.size += 1

    def insertTail(self, val: int) -> None:
        current = self.head
        while current.next:
            current = current.next
        current.next = LinkedListNode(None, val)
        self.size += 1

    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.size:
            return False
        prev, i = self.head, index
        while i > 0:
            prev = prev.next
            i -= 1
        val = prev.next.value
        prev.next = prev.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        current, result = self.head.next, []
        while current:
            result.append(current.value)
            current = current.next
        return result