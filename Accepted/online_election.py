"""
https://leetcode.com/problems/online-election/
"""


from collections import Counter
from bisect import bisect_right


class TopVotedCandidate:

    def __init__(self, persons: list[int], times: list[int]):
        self.leaders = []
        self.times = times
        cnt = Counter()
        currLeader = -1
        for p in persons:
            cnt[p] += 1
            if cnt[p] >= cnt[currLeader]:
                currLeader = p

            self.leaders.append(currLeader)

    def q(self, t: int) -> int:
        return self.leaders[bisect_right(self.times, t) - 1]


t = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
