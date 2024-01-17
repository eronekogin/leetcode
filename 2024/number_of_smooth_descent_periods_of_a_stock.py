"""
https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/description/
"""


class Solution:
    """
    Solution
    """

    def get_descent_periods(self, prices: list[int]) -> int:
        """
        get_descent_periods
        """
        start, end, n = 0, 0, len(prices)
        rslt = 0
        while end < n:
            while end + 1 < n and prices[end + 1] + 1 == prices[end]:
                end += 1

            curr_len = end - start + 1
            rslt += (1 + curr_len) * curr_len // 2
            end += 1
            start = end

        return rslt


print(Solution().get_descent_periods(
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7]))
