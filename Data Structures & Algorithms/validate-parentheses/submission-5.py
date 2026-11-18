class Solution:
    map = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    def isValid(self, s: str) -> bool:
        stack = Stack()
        for c in s:
            if c not in self.map.keys():
                stack.push(c)
                continue
            if stack.pop() != self.map[c]:
                return False
        return stack.isEmpty()

class Stack:
    def __init__(self) -> None:
        self.cache = []

    def isEmpty(self):
        return not self.cache

    def peek(self):
        return self.cache[-1] if self.cache else None

    def push(self, element):
        self.cache.append(element)

    def pop(self):
        return self.cache.pop() if self.cache else None