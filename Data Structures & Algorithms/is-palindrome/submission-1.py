class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            leftChar, rightChar = s[left].lower(), s[right].lower()
            if not leftChar.isalnum():
                left += 1
                continue
            if not rightChar.isalnum():
                right -= 1
                continue
            if leftChar != rightChar:
                return False
            left += 1
            right -= 1
        return True