class Solution:
    def searchRow(self, row, target) -> bool:
        left, right = 0, len(row) - 1
        while left <= right:
            middle = (left + right) // 2
            if target == row[middle]:
                return True
            if target < row[middle]:
                right = middle - 1
            else:
                left = middle + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowRowIndex, highRowIndex = 0, len(matrix) - 1
        while lowRowIndex <= highRowIndex:
            middleRowIndex = (lowRowIndex + highRowIndex) // 2
            middleRow = matrix[middleRowIndex]
            if middleRow[0] <= target <= middleRow[-1]:
                return self.searchRow(middleRow, target)
            if target < middleRow[0]:
                highRowIndex = middleRowIndex - 1
            else:
                lowRowIndex = middleRowIndex + 1
        return False