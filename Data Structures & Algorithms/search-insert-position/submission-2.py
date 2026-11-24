class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result = n
        leftPtr, rightPtr = 0, n - 1
        while leftPtr <= rightPtr:
            midPtr = (leftPtr + rightPtr) // 2
            mid = nums[midPtr]
            if mid == target:
                return midPtr
            elif mid < target:
                leftPtr = midPtr + 1
            else:
                rightPtr = midPtr - 1
                result = midPtr
        return result