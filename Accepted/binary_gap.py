"""
https://leetcode.com/problems/binary-gap/
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        x = n
        maxLen = 0
        while x & 1 == 0:  # Found the first non-zero digit.
            x >>= 1

        currLen = 0  # Initial length is zero.
        while x:
            if x & 1:
                maxLen = max(maxLen, currLen)
                currLen = 1
            else:
                currLen += 1

            x >>= 1

        return maxLen


print(Solution().binaryGap(8))
