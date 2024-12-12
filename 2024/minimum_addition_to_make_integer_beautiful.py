"""
https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/description/
"""


class Solution:
    """
    Solution
    """

    def make_integer_beautiful(self, n: int, target: int) -> int:
        """
        make integer beautiful
        """
        digits = [int(c) for c in str(n)]
        total = sum(digits)
        if total <= target:
            return 0

        cnt = 0
        n = len(digits)
        for i in range(n):
            x = digits[n - 1 - i]
            cnt += (10 - x) * (10 ** i)
            total = total - x + 1
            if total <= target:
                break

            digits[n - 1 - i - 1] += 1

        return cnt
