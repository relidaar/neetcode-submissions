class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for sChar, tChar in zip(s, t):
            count[sChar] = count.get(sChar, 0) + 1
            count[tChar] = count.get(tChar, 0) - 1
        remainder = [c for c, v in count.items() if v != 0]
        return not remainder