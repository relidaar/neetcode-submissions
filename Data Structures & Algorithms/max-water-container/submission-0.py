class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left, right = 0, len(heights) - 1
        while left < right:
            leftHeight, rightHeight = heights[left], heights[right]
            area = (right - left) * min(leftHeight, rightHeight)
            maxArea = max(maxArea, area)
            if leftHeight < rightHeight:
                left += 1
            else:
                right -= 1
        return maxArea
        