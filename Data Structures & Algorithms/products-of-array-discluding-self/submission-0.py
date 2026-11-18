class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProducts, suffixProducts = [], []
        for i in range(len(nums)):
            prefixProduct = self.get(prefixProducts, i - 1)
            prefixNum = self.get(nums, i - 1)
            prefixProducts.append(prefixProduct * prefixNum)

            suffixProduct = self.get(suffixProducts, len(suffixProducts) - i)
            suffixNum = self.get(nums, len(nums) - i)
            suffixProducts.insert(0, suffixProduct * suffixNum)
        return [prefix * suffix for prefix, suffix in zip(prefixProducts, suffixProducts)]

    def get(self, nums, i):
        return nums[i] if 0 <= i < len(nums) else 1