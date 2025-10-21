"""
https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def number_of_beautiful_integers(self, low: int, high: int, k: int) -> int:
        """
        number of beautiful integers
        """
        @cache
        def dfs(
            s: str,
            i: int,
            odds: int,
            evens: int,
            remainder: int,
            is_tight: bool,
            is_leading_zero: bool
        ):
            if i >= len(s):
                return remainder % k == 0 and odds == evens

            curr = int(s[i])
            bound = curr if is_tight else 9
            cnt = 0
            for d in range(bound + 1):
                add_to_odds = d & 1 == 1
                add_to_evens = d & 1 == 0
                if is_leading_zero and d == 0:
                    add_to_evens = 0

                cnt += dfs(
                    s,
                    i + 1,
                    odds + add_to_odds,
                    evens + add_to_evens,
                    (remainder * 10 + d) % k,
                    is_tight and d == curr,
                    is_leading_zero and d == 0
                )

            return cnt

        return dfs(str(high), 0, 0, 0, 0, True, True) - dfs(str(low - 1), 0, 0, 0, 0, True, True)


print(Solution().number_of_beautiful_integers(36, 60, 3))
