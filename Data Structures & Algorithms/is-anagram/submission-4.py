class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cache = dict()
        for letter in s:
            cache[letter] = cache.get(letter, 0) + 1
        for letter in t:
            cache[letter] = cache.get(letter, 0) - 1
        for letter, count in cache.items():
            if count != 0:
                return False
        return True