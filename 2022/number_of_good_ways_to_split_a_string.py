"""
https://leetcode.com/problems/number-of-good-ways-to-split-a-string/
"""


from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        cnt = 0
        left, right = Counter(), Counter(s)
        for c in s:
            left[c] += 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]

            if len(left) == len(right):
                cnt += 1

        return cnt
