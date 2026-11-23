class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        writePtr = readPtr = 0
        currentNumber = 0
        while currentNumber <= 2:
            if readPtr >= len(nums):
                currentNumber += 1
                readPtr = writePtr
            elif nums[writePtr] == currentNumber:
                writePtr += 1
                readPtr = writePtr
            elif nums[readPtr] == currentNumber:
                nums[writePtr], nums[readPtr] = nums[readPtr], nums[writePtr]
            else:
                readPtr += 1