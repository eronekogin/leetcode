"""
https://leetcode.com/problems/count-the-number-of-powerful-integers/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_powerful_int(self, start: int, finish: int, limit: int, s: str) -> int:
        """
        number of powerful int
        """
        def calc(x: str) -> int:
            if len(x) < len(s):
                return 0

            if len(x) == len(s):
                return int(x >= s)

            prev = len(x) - len(s)
            cnt = 0

            for i in range(prev):
                if limit < int(x[i]):
                    cnt += (limit + 1) ** (prev - i)
                    return cnt

                cnt += int(x[i]) * (limit + 1) ** (prev - 1 - i)

            if x[prev:] >= s:
                cnt += 1

            return cnt

        return calc(str(finish)) - calc(str(start - 1))
