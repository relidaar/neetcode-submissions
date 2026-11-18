class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            leftNum, rightNum = numbers[left], numbers[right]
            numSum = leftNum + rightNum
            if numSum == target:
                return [left + 1, right + 1]
            elif numSum < target:
                left += 1
            else:
                right -= 1
        return []