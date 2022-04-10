"""
https://leetcode.com/problems/guess-number-higher-or-lower/
"""


def guess(num: int) -> int:
    targetNum = 2
    if targetNum < num:
        return -1
    elif targetNum > num:
        return 1
    else:
        return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while start <= end:
            middle = start + ((end - start) >> 1)
            guessRslt = guess(middle)
            if guessRslt == 1:  # Target number is larger.
                start = middle + 1
            elif guessRslt == -1:  # Target number is smaller.
                end = middle - 1
            else:  # Found.
                return middle


print(Solution().guessNumber(2))
