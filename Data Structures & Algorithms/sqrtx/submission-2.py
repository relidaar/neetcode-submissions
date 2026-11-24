class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        left, right = 1, x // 2
        result = -1
        while left <= right:
            mid = (left + right) // 2
            midDoubled = mid ** 2
            if midDoubled == x:
                return mid
            elif midDoubled < x:
                left = mid + 1
                result = mid
            else:
                right = mid - 1
        return result