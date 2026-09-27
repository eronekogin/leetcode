"""
https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/description/
"""


class Solution:
    """
    Solution
    """

    def min_changes(self, n: int, k: int) -> int:
        """
        min changes
        """
        i = 0
        cnt = 0
        max_num = max(n, k)
        while (1 << i) <= max_num:
            x = n & (1 << i)
            y = k & (1 << i)

            if x != y:
                if x == 0:
                    return -1

                cnt += 1

            i += 1

        return cnt
