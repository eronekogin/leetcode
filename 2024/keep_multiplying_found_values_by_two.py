"""
https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/
"""


class Solution:
    """
    Solution
    """

    def find_final_value(self, nums: list[int], original: int) -> int:
        """
        find_final_value
        """
        curr = original
        candidates = set(nums)
        while curr in candidates:
            curr <<= 1

        return curr
