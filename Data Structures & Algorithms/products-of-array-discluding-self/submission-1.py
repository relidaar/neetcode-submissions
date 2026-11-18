class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [1] * n
        for i in range(1, n):
            products[i] = nums[i-1] * products[i-1]
        reverse_product = nums[-1]
        for i in range(n-2, -1, -1):
            products[i] *= reverse_product
            reverse_product *= nums[i]
        return products