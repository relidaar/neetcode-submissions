class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPtr, rightPtr = 0, len(numbers) - 1
        while leftPtr < rightPtr:
            valuesSum = numbers[leftPtr] + numbers[rightPtr]
            if valuesSum == target:
                return [leftPtr + 1, rightPtr + 1]
            elif valuesSum < target:
                leftPtr += 1
            elif valuesSum > target:
                rightPtr -= 1
            