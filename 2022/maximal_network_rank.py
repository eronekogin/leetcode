"""
https://leetcode.com/problems/maximal-network-rank/
"""


class Solution:
    def maximalNetworkRank(self, n: int, roads: list[list[int]]) -> int:
        roadCnt = [0] * n
        pairMemo: set[tuple[int, int]] = set()
        for a, b in roads:
            roadCnt[a] += 1
            roadCnt[b] += 1
            pairMemo.add((a, b))

        # Sort the cities from most input roads to least.
        sortedCities = sorted(range(n), key=lambda x: -roadCnt[x])
        maxRank = 0
        for a in range(n):
            for b in range(a + 1, n):
                cityA, cityB = sortedCities[a], sortedCities[b]
                score = roadCnt[cityA] + roadCnt[cityB]
                if (cityA, cityB) in pairMemo or (cityB, cityA) in pairMemo:
                    score -= 1

                if score < maxRank:
                    return maxRank

                maxRank = score

        return maxRank
