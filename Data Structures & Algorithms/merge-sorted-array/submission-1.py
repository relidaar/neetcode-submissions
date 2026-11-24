class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        writeCursor = ReverseCursor(nums1, 0, len(nums1) - 1)
        nums1Cursor = ReverseCursor(nums1, 0, m - 1)
        nums2Cursor = ReverseCursor(nums2, 0, len(nums2) - 1)
        while writeCursor.isValid():
            value = self.getGreatestValue(nums1Cursor, nums2Cursor)
            writeCursor.setValue(value)
            writeCursor.advance()

    def getGreatestValue(self, source1Cursor: 'ReverseCursor', source2Cursor: 'ReverseCursor') -> int:
        if source1Cursor.isValid() and not source2Cursor.isValid():
            result = source1Cursor.getValue()
            source1Cursor.advance()
            return result
        elif not source1Cursor.isValid() and source2Cursor.isValid():
            result = source2Cursor.getValue()
            source2Cursor.advance()
            return result
        value1, value2 = source1Cursor.getValue(), source2Cursor.getValue()
        if value1 > value2:
            source1Cursor.advance()
            return value1
        else:
            source2Cursor.advance()
            return value2


class ReverseCursor:
    def __init__(self, source: List[int], start: int, end: int) -> None:
        self.source = source
        self.ptr = end
        self.start = start
        self.end = end
    
    def isValid(self):
        return self.ptr >= self.start

    def advance(self):
        self.ptr -= 1

    def getValue(self):
        return self.source[self.ptr]
    
    def setValue(self, value):
        self.source[self.ptr] = value