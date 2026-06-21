"""
https://leetcode.com/problems/maximum-prime-difference/description/
"""


CANDIDATES = {
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
}


class Solution:
    """
    Solution
    """

    def maximum_prime_difference(self, nums: list[int]) -> int:
        """
        maximum prime difference
        """
        first = -1
        for i, x in enumerate(nums):
            if x in CANDIDATES:
                first = i
                break

        if first < 0:
            return 0

        n = len(nums)
        last = n
        for i in range(n - 1, first - 1, -1):
            if nums[i] in CANDIDATES:
                last = i
                break

        if last == n:
            return 0

        return last - first
