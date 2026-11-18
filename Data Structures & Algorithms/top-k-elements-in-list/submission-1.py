class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cache = {}
        for num in nums:
            cache[num] = cache.get(num, 0) + 1
        groups =  [[] for i in range(len(nums))]
        for num, count in cache.items():
            groups[count - 1].append(num)
        result = []
        for group in reversed(groups):
            for num in group:
                result.append(num)
                if len(result) == k:
                    return result
        return []
