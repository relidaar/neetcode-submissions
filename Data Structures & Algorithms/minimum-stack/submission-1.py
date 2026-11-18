class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        # append min element
        self.stack.append(min(self.stack[-2], val) if self.stack else val)
        self.stack.append(val)

    def pop(self) -> None:
        # pop min element
        self.stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[-2]
