"""
https://leetcode.com/problems/count-special-integers/description/
"""


from math import perm


class Solution:
    """
    Solution
    """

    def count_special_numbers(self, n: int) -> int:
        """
        count special numbers
        """
        digits = [int(c) for c in str(n + 1)]
        size = len(digits)
        cnt = sum(9 * perm(9, i) for i in range(size - 1))

        visited: set[int] = set()
        for i, d in enumerate(digits):
            # Must be positive integer, so the first digit
            # cannot start with 0
            for d2 in range(i == 0, d):
                if d2 not in visited:
                    cnt += perm(9 - i, size - i - 1)

            if d in visited:
                break

            visited.add(d)

        return cnt
