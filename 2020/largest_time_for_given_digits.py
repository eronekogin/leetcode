"""
https://leetcode.com/problems/largest-time-for-given-digits/
"""


from typing import List
from itertools import permutations


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        maxTime = max(
            [
                (h, m)
                for h, m in map(
                    lambda x: (10 * x[0] + x[1], 10 * x[2] + x[3]),
                    permutations(A))
                if h < 24 and m < 59
            ] or [''])

        if maxTime:
            return '{:02d}:{:02d}'.format(*maxTime)

        return maxTime


print(Solution().largestTimeFromDigits([1, 2, 3, 4]))
