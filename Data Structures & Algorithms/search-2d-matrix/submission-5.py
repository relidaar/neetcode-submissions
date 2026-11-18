class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            row = matrix[mid]
            if row[0] <= target <= row[-1]:
                return self.searchRow(row, target)
            elif target < row[0]:
                bottom = mid - 1
            elif target > row[-1]:
                top = mid + 1
        return False

    def searchRow(self, row: List[int], target: int) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            midValue = row[mid]
            if midValue == target:
                return True
            elif midValue < target:
                left = mid + 1
            elif midValue > target:
                right = mid - 1
        return False