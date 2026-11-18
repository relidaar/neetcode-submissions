class Solution:
    valid_parens = ['()', '[]', '{}']

    def isValid(self, s: str) -> bool:
        cache = []
        for paren in s:
            if paren in '({[':
                cache.append(paren)
                continue
            if not cache:
                return False
            opening_paren = cache.pop()
            if opening_paren + paren not in self.valid_parens:
                return False
        return not cache
