"""
https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/
"""


class Solution:
    """
    Solution
    """

    def punishment_number(self, n: int) -> int:
        """
        punishment number
        """
        def is_candidate(x: int, t: int):
            if x == t:
                return True

            if x == 0:
                return t == 0

            for m in mod_range:
                q, r = divmod(x, m)
                if is_candidate(q, t - r):
                    return True

            return False

        mod_range = [10, 100, 1000]
        return sum(
            i * i
            for i in range(1, n + 1)
            if is_candidate(i * i, i)
        )
