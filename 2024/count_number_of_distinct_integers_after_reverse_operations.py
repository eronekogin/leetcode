"""
https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/
"""


class Solution:
    """
    Solution
    """

    def count_distinct_integers(self, nums: list[int]) -> int:
        """
        count distinct integers
        """
        memo: set[str] = set()
        for s in map(str, nums):
            memo.add(s)
            memo.add(s[::-1].lstrip('0'))

        return len(memo)
