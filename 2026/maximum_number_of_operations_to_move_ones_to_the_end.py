"""
https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/description/
"""


class Solution:
    """
    Solution
    """

    def max_operations(self, s: str) -> int:
        """
        max operations
        """
        prev_ones = 0
        i, n = 0, len(s)
        rslt = 0

        while i < n:
            if s[i] == '0':
                while i + 1 < n and s[i + 1] == '0':
                    i += 1

                rslt += prev_ones
            else:
                prev_ones += 1

            i += 1

        return rslt


print(Solution().max_operations('1001101'))
