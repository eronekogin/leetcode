"""
https://leetcode.com/problems/maximum-product-of-three-numbers/
"""


from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        sn = sorted(nums)
        return max(
            sn[0] * sn[1] * sn[-1], sn[-3] * sn[-2] * sn[-1])

    def maximumProduct2(self, nums: List[int]) -> int:
        """
        Single scan to find the above minimum and maximum numbers.
        """
        min1 = min2 = float('inf')
        max1 = max2 = max3 = float('-inf')
        for num in nums:
            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num

        return max(min1 * min2 * max1, max1 * max2 * max3)


print(Solution().maximumProduct2([1, 2, 3, 2]))
