class Solution:
    separator = '/'

    def encode(self, strs: List[str]) -> str:
        result = ''
        for s in strs:
            result += str(len(s)) + self.separator + s
        return result

    def decode(self, s: str) -> List[str]:
        result, it = [], 0
        while it < len(s) - 1:
            count = ''
            while s[it] != self.separator:
                count += s[it]
                it += 1
            it += 1
            
            word = ''
            for _ in range(int(count)):
                word += s[it]
                it += 1
            result.append(word) 
        return result