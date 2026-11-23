class MyHashMap:

    def __init__(self):
        self.size = 10007
        self.cache: List[Optional[HashMapNode]] = [None] * self.size

    def __calculateIndex(self, key: int) -> int:
        return key % self.size

    def __findNode(self, key: int) -> Optional['HashMapNode']:
        index = self.__calculateIndex(key)
        if not self.cache[index]:
            return None
        node = self.cache[index]
        while node:
            if node.key == key:
                return node
            node = node.next
        return None

    def __add(self, key: int, value: int) -> None:
        index = self.__calculateIndex(key)
        if not self.cache[index]:
            self.cache[index] = HashMapNode(index, key, value)
        else:
            node = self.cache[index]
            while node.next:
                node = node.next
            node.next = HashMapNode(index, key, value, prev=node)

    def put(self, key: int, value: int) -> None:
        node = self.__findNode(key)
        if node:
            node.value = value
        else:
            self.__add(key, value)

    def get(self, key: int) -> int:
        node = self.__findNode(key)
        return node.value if node else -1

    def remove(self, key: int) -> None:
        node = self.__findNode(key)
        if not node:
            return None
        elif self.cache[node.index] == node:
            self.cache[node.index] = None
        else:
            node.prev = node.next

class HashMapNode:
    def __init__(self, index: int, key: int, value: int, next: Optional['HashMapNode'] = None, prev: Optional['HashMapNode'] = None) -> None:
        self.index = index
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)