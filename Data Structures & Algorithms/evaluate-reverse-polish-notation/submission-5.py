import math

class Solution:
    def operation(self, left, operator, right):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            return int(left / right)
        raise Exception("Invalid operation")

    def is_number(self, s):
        try:
            int(s)
        except ValueError:  # Failed
            return False
        else:  # Succeeded
            return True

    def evalRPN(self, tokens: List[str]) -> int:
        cache = []
        for token in tokens:
            if self.is_number(token):
                cache.append(int(token))
                continue
            right = cache.pop()
            left = cache.pop()
            result = self.operation(left, token, right)
            cache.append(result)
        return cache.pop()