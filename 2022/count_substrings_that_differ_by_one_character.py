"""
https://leetcode.com/problems/count-substrings-that-differ-by-one-character/
"""


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        def check(i1: int, i2: int) -> int:
            cnt = prev = curr = 0
            for j in range(min(L1 - i1, L2 - i2)):
                curr += 1
                if s[i1 + j] != t[i2 + j]:
                    prev, curr = curr, 0

                cnt += prev

            return cnt

        L1, L2 = len(s), len(t)
        return sum(check(i1, 0) for i1 in range(L1)) + sum(check(0, i2) for i2 in range(1, L2))
