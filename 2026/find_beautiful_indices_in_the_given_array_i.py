"""
https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/description/
"""


class Solution:
    """
    Solution
    """

    def beautiful_indices(self, s: str, a: str, b: str, k: int) -> list[int]:
        """
        beautiful indices
        """
        i, j = s.find(a), s.find(b)
        rslt: list[int] = []

        while i >= 0 and j >= 0:
            if abs(i - j) <= k:
                rslt.append(i)
                i = s.find(a, i + 1)
            elif i > j:
                j = s.find(b, i - k)
            else:
                i = s.find(a, j - k)

        return rslt


print(Solution().beautiful_indices(
    'rinzbrrr', 'nzb', 'r', 2))
