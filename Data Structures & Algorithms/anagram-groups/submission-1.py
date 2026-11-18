import hashlib

class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        result = dict()
        for word in words:
            key = ''.join(c for c in sorted(word))
            if key not in result:
                result[key] = []
            result[key].append(word)
        return list(result.values())