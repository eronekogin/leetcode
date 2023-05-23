"""
https://leetcode.com/problems/maximum-population-year/
"""


class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        cnt = [0] * 101
        for birth, death in logs:
            for i in range(birth, death):
                cnt[i - 1950] += 1

        maxPop = max(cnt)
        return 1950 + cnt.index(maxPop)
