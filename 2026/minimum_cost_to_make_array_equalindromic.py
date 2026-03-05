"""
https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, nums: list[int]) -> int:
        """
        minimum cost
        """
        def is_pal(x: int) -> bool:
            t = str(x)
            return t == t[::-1]

        nums.sort()
        l = r = nums[len(nums) >> 1]

        while not is_pal(l):
            l -= 1

        while not is_pal(r):
            r += 1

        return min(
            sum(abs(x - l) for x in nums),
            sum(abs(x - r) for x in nums)
        )
