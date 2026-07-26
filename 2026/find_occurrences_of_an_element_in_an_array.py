"""
https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def occurrences_of_element(self, nums: list[int], queries: list[int], x: int) -> list[int]:
        """
        occurrences of element
        """
        memo = [i for i, y in enumerate(nums) if y == x]
        return [
            memo[q - 1] if q - 1 < len(memo) else -1
            for q in queries
        ]
