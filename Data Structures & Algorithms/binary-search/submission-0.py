class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            midNum = nums[mid]
            if midNum == target:
                return mid
            elif midNum < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1