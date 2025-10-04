"""
https://leetcode.com/problems/count-stepping-numbers-in-range/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def count_stepping_numbers(self, low: str, high: str) -> int:
        """
        count stepping numbers
        """
        def count(s: str) -> int:
            @cache
            def dp(
                i: int,
                is_tight: bool,
                last_digit: int,
            ) -> int:
                if i == len(s):
                    return 1

                max_digit = int(s[i]) if is_tight else 9
                rslt = 0

                for d in range(max_digit + 1):
                    is_next_tight = is_tight and d == max_digit
                    if last_digit == -1:
                        d = -1 if d == 0 else d
                        rslt = (
                            rslt +
                            dp(
                                i + 1,
                                is_next_tight,
                                d
                            )
                        ) % mod
                    elif abs(last_digit - d) == 1:
                        rslt = (
                            rslt +
                            dp(
                                i + 1,
                                is_next_tight,
                                d,
                            )
                        ) % mod

                return rslt

            return dp(0, True, -1)

        mod = 10 ** 9 + 7
        return (count(high) - count(str(int(low) - 1))) % mod
