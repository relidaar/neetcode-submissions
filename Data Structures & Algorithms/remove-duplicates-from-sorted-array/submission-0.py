class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        writePtr = readPtr = 0
        while readPtr < len(nums):
            if nums[readPtr] == nums[writePtr]:
                readPtr += 1
            elif nums[readPtr] > nums[writePtr]:
                writePtr += 1
                nums[writePtr] = nums[readPtr]
                count += 1
        return count