"""
https://leetcode.com/problems/count-integers-with-even-digit-sum/description/
"""


class Solution:
    """
    Solution
    """

    def count_even(self, num: int) -> int:
        """
        count even
        """
        total_sum = sum(int(c) for c in str(num))
        return (num - (total_sum & 1)) >> 1
