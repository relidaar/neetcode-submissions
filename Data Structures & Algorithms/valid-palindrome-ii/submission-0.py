class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.__isPalindrome(s, 0, len(s) - 1, 1)

    def __isPalindrome(self, source: str, start: int, end: int, maxRecursion: int) -> bool:
        left, right = start, end
        while left < right:
            leftCharacter, rightCharacter = source[left].lower(), source[right].lower()
            if not leftCharacter.isalnum():
                left += 1
            elif not rightCharacter.isalnum():
                right -= 1
            elif leftCharacter != rightCharacter:
                return maxRecursion > 0 \
                        and (self.__isPalindrome(source, left +  1, right, 0) \
                        or self.__isPalindrome(source, left, right - 1, 0))
            else:
                left += 1
                right -= 1
        return True