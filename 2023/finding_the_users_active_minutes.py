"""
https://leetcode.com/problems/finding-the-users-active-minutes/
"""


from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        uam = defaultdict(set)
        for id, minute in logs:
            uam[id].add(minute)

        uamFreq = [0] * k
        for x in uam.values():
            if len(x) <= k:
                uamFreq[len(x) - 1] += 1

        return uamFreq
