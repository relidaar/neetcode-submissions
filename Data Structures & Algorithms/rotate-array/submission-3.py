class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    def reverse(self, source: List[int], leftPtr: int, rightPtr: int) -> None:
        while leftPtr < rightPtr:
            source[leftPtr], source[rightPtr] = source[rightPtr], source[leftPtr]
            leftPtr += 1
            rightPtr -= 1