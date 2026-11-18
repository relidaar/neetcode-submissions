class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for p in s:
            if p not in parens:
                stack.append(p)
                continue
            if not stack:
                return False
            lastParen = stack[-1]
            if lastParen != parens[p]:
                return False
            stack.pop()
        return not stack