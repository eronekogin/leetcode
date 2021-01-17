"""
https://leetcode.com/problems/count-sorted-vowel-strings/
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        cnt = [1] * 5
        for _ in range(n - 1):
            cnt[3] += cnt[4]
            cnt[2] += cnt[3]
            cnt[1] += cnt[2]
            cnt[0] += cnt[1]

        return sum(cnt)
