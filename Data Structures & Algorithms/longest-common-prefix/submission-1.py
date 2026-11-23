class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        minWordLen = min([len(word) for word in words])
        commonPrefix = ''
        for index in range(minWordLen):
            prefixCharacter = words[0][index]
            for word in words:
                if word[index] != prefixCharacter:
                    return commonPrefix
            commonPrefix += prefixCharacter
        return commonPrefix