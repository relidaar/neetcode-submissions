class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        for token in tokens[1:]:
            if self.isnum(token):
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

    def isnum(self, s):
        try: 
            int(s)
        except ValueError:
            return False
        else:
            return True