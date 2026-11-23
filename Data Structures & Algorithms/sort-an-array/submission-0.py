class Solution:
    def __merge(self, left: List[int], right: List[int]) -> List[int]:
        temp = []
        leftCursor, rightCursor = ListCursor(left), ListCursor(right)
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
        return temp

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left, right = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])
        return self.__merge(left, right)

class ListCursor:
    def __init__(self, source: List[int]) -> None:
        self.ptr = 0
        self.source = source

    def isValid(self) -> bool:
        return self.ptr < len(self.source)
    
    def advance(self) -> 'ListCursor':
        self.ptr += 1
        return self

    def get(self) -> int:
        return self.source[self.ptr]