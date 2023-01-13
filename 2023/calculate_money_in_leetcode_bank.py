"""
https://leetcode.com/problems/calculate-money-in-leetcode-bank/
"""


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, remainDays = divmod(n, 7)
        totalMoney = 0
        if weeks > 0:
            lastMondayMoney = weeks + 1
            totalMoney += (((4 + 4 + weeks - 1) * weeks) >> 1) * 7
        else:
            lastMondayMoney = 1

        return totalMoney + (
            (
                (
                    lastMondayMoney +
                    lastMondayMoney +
                    remainDays - 1
                ) * remainDays
            ) >> 1
        )


print(Solution().totalMoney(20))
