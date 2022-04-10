"""
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = start = 0
        memo = {c: 0 for c in 'abc'}
        for c in s:
            memo[c] += 1
            while all(memo.values()):
                memo[s[start]] -= 1
                start += 1

            cnt += start

        return cnt
