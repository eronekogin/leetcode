"""
https://leetcode.com/problems/find-the-town-judge/
"""


from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        memo = {}
        sumTrust = 0
        for a, b in trust:
            if a not in memo:
                sumTrust += a
                memo[a] = {b}
            else:
                memo[a].add(b)

        if len(memo) != N - 1:
            return -1

        rslt = (((1 + N) * N) >> 1) - sumTrust
        for labels in memo.values():
            if rslt not in labels:
                return -1

        return rslt
