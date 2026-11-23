class Solution:
    def __merge(self, left: 'ListView', right: 'ListView') -> None:
        temp = []
        leftCursor, rightCursor = left.cursor(), right.cursor()
        while leftCursor.isValid() and rightCursor.isValid():
            leftEl, rightEl = leftCursor.get(), rightCursor.get()
            if leftEl < rightEl:
                temp.append(leftEl)
                leftCursor.advance()
            else:
                temp.append(rightEl)
                rightCursor.advance()
        while leftCursor.isValid():
            temp.append(leftCursor.get())
            leftCursor.advance()
        while rightCursor.isValid():
            temp.append(rightCursor.get())
            rightCursor.advance()
        tempCursor = ListView(temp, 0, len(temp) - 1).cursor()
        for i in range(left.size):
            left.set(i, tempCursor.get())
            tempCursor.advance()
        for i in range(right.size):
            right.set(i, tempCursor.get())
            tempCursor.advance()

    def __sortArray(self, nums: 'ListView') -> None:
        if nums.size <= 1:
            return
        mid = (nums.start + nums.end) // 2
        left = ListView(nums.source, nums.start, mid)
        right = ListView(nums.source, mid + 1, nums.end)
        self.__sortArray(left)
        self.__sortArray(right)
        self.__merge(left, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.__sortArray(ListView(nums, 0, len(nums) - 1))
        return nums

class ListView:
    def __init__(self, source: List[int], start: int, end: int) -> None:
        self.source = source
        self.start = start
        self.end = end
        self.size = self.end + 1 - self.start

    def cursor(self) -> 'ListViewCursor':
        return ListViewCursor(self)

    def get(self, index: int) -> int:
        return self.source[self.start + index]

    def set(self, index: int, value: int) -> None:
        self.source[self.start + index] = value

    def getFirst(self) -> int:
        return self.get(0)

    def __str__(self) -> str:
        return str(self.source[self.start:self.end + 1])

class ListViewCursor:
    def __init__(self, source: ListView) -> None:
        self.ptr = 0
        self.source = source

    def isValid(self) -> bool:
        return self.ptr < self.source.size
    
    def advance(self) -> None:
        self.ptr += 1

    def get(self) -> int:
        return self.source.get(self.ptr)