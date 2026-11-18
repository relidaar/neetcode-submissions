class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            leftCharacter, rightCharacter = s[left].lower(), s[right].lower()
            if not leftCharacter.isalnum():
                left += 1
            elif not rightCharacter.isalnum():
                right -= 1
            elif leftCharacter != rightCharacter:
                return False
            else:
                left += 1
                right -= 1
        return True