class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        readPtr, writePtr = 0, 0
        placeholder = -1
        while readPtr < len(nums):
            if nums[readPtr] == val:
                nums[readPtr] = placeholder
                readPtr += 1
            elif nums[writePtr] == placeholder:
                nums[writePtr], nums[readPtr] = nums[readPtr], placeholder
                readPtr += 1
                writePtr += 1
            else:
                readPtr += 1
                writePtr += 1
        k = 0
        for num in nums:
            if num == placeholder:
                break
            k += 1
        return k