"""
https://leetcode.com/problems/sequential-digits/
"""


from typing import List
from math import log10


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lowLen, highLen = int(log10(low)) + 1, int(log10(high)) + 1

        rslt = []
        for maxLen in range(lowLen, min(highLen + 1, 10)):
            for start in range(10 - maxLen):
                currNum = sum(
                    (start + i) * 10 ** (maxLen - i)
                    for i in range(1, maxLen + 1))

                if currNum > high:
                    break
                elif currNum >= low:
                    rslt.append(currNum)

        return rslt


print(Solution().sequentialDigits(10, 10 ** 9))
