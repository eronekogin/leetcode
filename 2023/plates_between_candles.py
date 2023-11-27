"""
https://leetcode.com/problems/plates-between-candles/
"""


from bisect import bisect_left, bisect_right


class Solution:
    """
    Solution
    """

    def plates_between_candles(self, s: str, queries: list[list[int]]) -> list[int]:
        """
        plates_between_candles
        """
        candle_indexes = [i for i, c in enumerate(s) if c == '|']
        rslt = [0] * len(queries)
        for i, (start, end) in enumerate(queries):
            # Found the first candle after start
            a = bisect_left(candle_indexes, start)

            # Found the last candle before end
            b = bisect_right(candle_indexes, end) - 1

            if a < b:
                # Number of length between the first and last candle is
                # candle_indexes[b] - candle_indexes[a] + 1
                #
                # Number of candles are b - a + 1
                #
                # So total candidate plates are
                # candle_indexes[b] - candle_indexes[a] + 1 - (b - a)
                rslt[i] = candle_indexes[b] - candle_indexes[a] + 1 - (b - a)

        return rslt


print(Solution().plates_between_candles("**|**|***|", [[2, 5], [5, 9]]))
