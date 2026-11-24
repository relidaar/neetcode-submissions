class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsSize = len(nums)
        k = k % numsSize
        swappedElementsCount = 0
        for startingIndex in range(numsSize):
            currentIndex = startingIndex
            temp = nums[startingIndex]
            while True: 
                nextIndex = (currentIndex + k) % numsSize
                nums[nextIndex], temp = temp, nums[nextIndex]
                swappedElementsCount += 1
                currentIndex = nextIndex
                if swappedElementsCount == numsSize:
                    return
                if currentIndex == startingIndex:
                    break