"""
https://leetcode.com/problems/minimum-operations-to-make-a-special-number/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_operations(self, num: str) -> int:
        """
        check 00, 25, 50, 75 pairs
        """
        n = len(num)
        min_ops = n + 1
        for i in range(n - 1, -1, -1):
            if num[i] == '5':
                for j in range(i - 1, -1, -1):
                    if num[j] == '2' or num[j] == '7':
                        # between = i - j - 1
                        # remain = n - 1 - i
                        # between + remain = n - j - 2
                        min_ops = min(min_ops, n - j - 2)
                        break

            if num[i] == '0':
                for j in range(i - 1, -1, -1):
                    if num[j] == '0' or num[j] == '5':
                        min_ops = min(min_ops, n - j - 2)
                        break

        if min_ops == n + 1:
            if '0' in num:
                return n - 1

            return n

        return min_ops
