class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagramGroups = dict()
        for string in strs:
            key = self.createKey(string)
            annagramGroups[key] = annagramGroups.get(key, [])
            annagramGroups[key].append(string)
        return [group for group in annagramGroups.values()]

    def createKey(self, string: str) -> str:
        cache = [0 for _ in range(26)]
        for letter in string:
            index = ord(letter) - 97
            cache[index] += 1
        return str(cache)