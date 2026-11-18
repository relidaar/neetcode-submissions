class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in cache:
                return [cache[remainder], i]
            cache[num] = i
        return []