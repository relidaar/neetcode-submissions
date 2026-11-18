class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache = {}
        for word in strs:
            frequencies = self.getFrequencies(word)
            anagrams = cache.get(frequencies, [])
            anagrams.append(word)
            cache[frequencies] = anagrams
        print(cache)
        return cache.values()
        
    def getFrequencies(self, s: str):
        result = [0] * 26
        for char in s:
            result[ord(char) - ord('a')] += 1
        return tuple(result)