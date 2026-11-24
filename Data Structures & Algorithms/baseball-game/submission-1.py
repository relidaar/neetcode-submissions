class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for operation in operations:
            if self.isNumber(operation):
                score.append(int(operation))
            elif operation == '+':
                score.append(score[-2] + score[-1])
            elif operation == 'D':
                score.append(score[-1] * 2)
            elif operation == 'C':
                score.pop()
        return sum(score)

    def isNumber(self, value: str):
        try:
            float(value)
            return True
        except ValueError:
            return False