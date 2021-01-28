"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/
"""


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        dupTimes, remainSum = divmod(k, 26)
        while dupTimes + remainSum < n:  # Not enough chars.
            dupTimes -= 1
            remainSum += 26

        rslt = ['z'] * dupTimes
        remainLen = n - dupTimes
        if remainLen:
            rslt.append(chr(ord('a') + remainSum - remainLen))
            rslt += ['a'] * (remainLen - 1)

        return ''.join(reversed(rslt))


print(Solution().getSmallestString(5, 130))
