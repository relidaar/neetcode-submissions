class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        top, bottom = 0, m - 1
        row = -1
        while True:
            if top > bottom:
                return False
            mid = (bottom + top) // 2
            midRow = matrix[mid]
            start, end = midRow[0], midRow[-1]
            if start <= target <= end:
                row = midRow
                break;
            elif target < start:
                bottom = mid - 1
            elif target > end:
                top = mid + 1
        return self.isInRow(row, target)            

    def isInRow(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]
            if midNum == target:
                return True
            elif midNum < target:
                left = mid + 1
            else:
                right = mid - 1
        return False