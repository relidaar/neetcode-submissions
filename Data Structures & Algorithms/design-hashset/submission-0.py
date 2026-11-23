class MyHashSet:

    def __init__(self):
        self.size = 10007
        self.cache: List[Optional[Node]] = [None] * self.size

    def calculateIndex(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.calculateIndex(key)
        if not self.cache[index]:
            self.cache[index] = Node(val=key)
        else:
            node = self.cache[index]
            while node.next:
                node = node.next
            node.next = Node(val=key, prev=node)

    def findNode(self, key: int) -> Optional[tuple[int, 'Node']]:
        index = self.calculateIndex(key)
        if not self.cache[index]:
            return None
        node = self.cache[index]
        while node:
            if node.val == key:
                return (index, node)
            node = node.next
        return None

    def remove(self, key: int) -> None:
        nodeTuple = self.findNode(key)
        if not nodeTuple:
            return None
        index, node = nodeTuple
        if self.cache[index] == node:
            self.cache[index] = None
        else:
            node.prev = node.next

    def contains(self, key: int) -> bool:
        return self.findNode(key) is not None

class Node:
    def __init__(self, val: int, next: Optional['Node'] = None, prev: Optional['Node'] = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)