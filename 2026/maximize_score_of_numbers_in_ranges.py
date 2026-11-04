"""
https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/description/
"""


from math import inf


class Solution:
    """
    Solution
    """
    def max_possible_score(self, start: list[int], d: int) -> int:
        """
        max possible score
        """
        def fn(m: int) -> bool:
            x = -inf

            for s in start:
                x += m
                if x > s + d:
                    return False

                x = max(x, s)

            return True

        start.sort()
        l, r = 0, 2 * 10 ** 9

        while l < r:
            m = (l + r + 1) // 2
            if fn(m):
                l = m
            else:
                r = m - 1

        return l
