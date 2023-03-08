"""
https://leetcode.com/problems/count-pairs-of-nodes/
"""

from collections import Counter


class Solution:
    def countPairs(
        self,
        n: int,
        edges: list[list[int]],
        queries: list[int]
    ) -> list[int]:
        degrees = [0] * n
        freqs = Counter()

        for u, v in edges:
            degrees[u - 1] += 1
            degrees[v - 1] += 1
            freqs[(min(u, v) - 1, max(u, v) - 1)] += 1

        sortedDegrees = sorted(degrees)
        rslt: list[int] = []

        for q in queries:
            cnt = 0
            l, r = 0, n - 1
            while l < r:
                if q < sortedDegrees[l] + sortedDegrees[r]:
                    # (l, r), (l + 1, r), ... , (r - 1, r) are all valid.
                    cnt += r - l
                    r -= 1
                else:
                    l += 1

            for u, v in freqs:
                sumDegrees = degrees[u] + degrees[v]
                if sumDegrees - freqs[(u, v)] <= q < sumDegrees:
                    cnt -= 1

            rslt.append(cnt)

        return rslt


print(Solution().countPairs(
    4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3]))
