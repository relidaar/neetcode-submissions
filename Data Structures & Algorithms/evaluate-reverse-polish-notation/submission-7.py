class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if self.isNumber(token):
                stack.append(int(token))
                continue
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))
        return stack.pop()

    def isNumber(self, token):
        try:
            int(token)
            return True
        except ValueError:
            return False