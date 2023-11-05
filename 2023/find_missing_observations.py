"""
https://leetcode.com/problems/find-missing-observations/
"""


class Solution:
    """
    Solution
    """

    def missing_rolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        """
        missing_rolls
        """
        m = len(rolls)
        total = (m + n) * mean
        remain = total - sum(rolls)

        if remain < n or remain > 6 * n:  # Not possible.
            return []

        mid, r = divmod(remain, n)
        rslt = [mid] * n
        for i in range(r):
            rslt[i] += 1

        return rslt
