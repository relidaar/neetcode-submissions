class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = dict()
        for c in s:
            cache[c] = cache.get(c, 0) + 1
        for c in t:
            cache[c] = cache.get(c, 0) - 1
        return all(val == 0 for val in cache.values())