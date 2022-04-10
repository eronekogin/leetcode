"""
https://leetcode.com/problems/powerful-integers/
"""

from math import log


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list[int]:
        if bound == 0:
            return []

        rslt = set()
        maxI = int(log(bound, x)) if x > 1 else 0
        maxJ = int(log(bound, y)) if y > 1 else 0
        for i in range(maxI + 1):
            left = x ** i
            for j in range(maxJ + 1):
                curr = left + y ** j
                if curr <= bound:
                    rslt.add(curr)

        return list(rslt)


print(Solution().powerfulIntegers(2, 3, 10))
