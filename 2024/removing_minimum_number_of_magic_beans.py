"""
https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_removal(self, beans: list[int]) -> int:
        """
        minimum_removal
        """
        n = len(beans)
        sorted_beans = sorted(beans)
        max_remain = max(
            sorted_beans[i] * (n - i)
            for i in range(n)
        )

        return sum(beans) - max_remain


print(Solution().minimum_removal([2, 10, 3, 2]))
