class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        while k > 0:
            start = 0
            end = start + k
            while end < len(nums):
                if nums[start] == nums[end]:
                    return True
                start += 1
                end += 1
            k -= 1
        return False