"""
https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
"""


class Solution:
    """
    Solution
    """

    def get_sneaky_numbers(self, nums: list[int]) -> list[int]:
        """
        get sneaky numbers
        """
        visited: set[int] = set()
        rslt: list[int] = []
        for x in nums:
            if x in visited:
                rslt.append(x)
                continue

            visited.add(x)

        return rslt
