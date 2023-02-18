"""
https://leetcode.com/problems/count-number-of-homogenous-substrings/
"""


class Solution:
    def countHomogenous(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1

        MOD = 10 ** 9 + 7
        cnt = 0
        start, end = 0, 1
        while end < N:
            if s[end] == s[start]:
                while end < N and s[end] == s[start]:
                    end += 1

            currLen = end - start
            cnt += (((1 + currLen) * currLen) >> 1) % MOD
            start = end

        return cnt % MOD
