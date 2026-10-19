"""
https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/description/
"""


class Solution:
    """
    Solution
    """

    def max_energy_boost(self, a: list[int], b: list[int]) -> int:
        """
        max energy boost
        """
        n = len(a)
        da = [0] * n
        db = [0] * n
        da[0] = a[0]
        db[0] = b[0]
        da[1] = a[0] + a[1]
        db[1] = b[0] + b[1]

        for i in range(2, n):
            da[i] = max(da[i - 1] + a[i], db[i - 2] + a[i])
            db[i] = max(db[i - 1] + b[i], da[i - 2] + b[i])

        return max(da[-1], db[-1])
