class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cache = dict()
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        for num, count in cache.items():
            if count > len(nums) / 2:
                return num
        return 0