"""
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/
"""


from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        def get_digits_sum(x: int):
            rslt = 0
            while x:
                x, r = divmod(x, 10)
                rslt += r

            return rslt

        cnt = Counter(
            get_digits_sum(x)
            for x in range(lowLimit, highLimit + 1)
        )

        return max(cnt.values())
