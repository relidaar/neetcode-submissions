class MyHashSet:

    def __init__(self):
        self.size = 10007
        self.cache: List[Optional[HashSetNode]] = [None] * self.size

    def __calculateIndex(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        index = self.__calculateIndex(key)
        if not self.cache[index]:
            self.cache[index] = HashSetNode(index, key)
        else:
            node = self.cache[index]
            while node.next:
                node = node.next
            node.next = HashSetNode(index, key, prev=node)

    def __findNode(self, key: int) -> Optional['HashSetNode']:
        index = self.__calculateIndex(key)
        if not self.cache[index]:
            return None
        node = self.cache[index]
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def remove(self, key: int) -> None:
        node = self.__findNode(key)
        if not node:
            return None
        elif self.cache[node.index] == node:
            self.cache[node.index] = None
        else:
            node.prev = node.next

    def contains(self, key: int) -> bool:
        return self.__findNode(key) is not None

class HashSetNode:
    def __init__(self, index: int, key: int, next: Optional['HashSetNode'] = None, prev: Optional['HashSetNode'] = None) -> None:
        self.index = index
        self.key = key
        self.next = next
        self.prev = prev

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)