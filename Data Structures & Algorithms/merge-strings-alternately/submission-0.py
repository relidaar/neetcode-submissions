class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result, word1Cursor, word2Cursor = '', ListCursor(word1), ListCursor(word2)
        while word1Cursor.isValid() or word2Cursor.isValid():
            result += word1Cursor.get()
            result += word2Cursor.get()
            word1Cursor.advance()
            word2Cursor.advance()
        return result

class ListCursor:
    def __init__(self, source):
        self.ptr = 0
        self.source = source

    def isValid(self):
        return self.ptr < len(self.source)

    def advance(self):
        self.ptr += 1

    def get(self):
        return self.source[self.ptr] if self.isValid() else ''