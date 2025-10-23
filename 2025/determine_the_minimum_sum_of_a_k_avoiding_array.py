"""
https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_sum(self, n: int, k: int) -> int:
        """
        minimum sum
        """
        m = k >> 1
        if m >= n:
            return ((1 + n) * n) >> 1

        remain = n - m

        return (
            (((1 + m) * m) >> 1) +
            (((k + k + remain - 1) * remain) >> 1)
        )


print(Solution().minimum_sum(2, 3))
