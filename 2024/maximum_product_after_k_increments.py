"""
https://leetcode.com/problems/maximum-product-after-k-increments/description/
"""


from heapq import heappush, heappop, heapify


class Solution:
    """
    Solution
    """

    def maximum_product(self, nums: list[int], k: int) -> int:
        """
        maximum product
        """
        heapify(nums)
        while k:
            heappush(nums, heappop(nums) + 1)
            k -= 1

        rslt = 1
        m = 10 ** 9 + 7
        for x in nums:
            rslt = (rslt * x) % m

        return rslt
