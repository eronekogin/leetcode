"""
https://leetcode.com/problems/minimum-cost-to-convert-string-ii/description/
"""

OFFSET = ord('a')
INF = 10**18
INF_INT = 10**9


class Solution:
    """
    Solution
    """

    def minimum_cost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        minimum cost
        """
        # Assign unique index for unique strings
        memo: dict[str, int] = {}
        for w in original:
            if w not in memo:
                memo[w] = len(memo)

        for w in changed:
            if w not in memo:
                memo[w] = len(memo)

        n = len(memo)
        d = [[float('inf')] * n for _ in range(n)]

        for x, y, c in zip(original, changed, cost):
            d[memo[x]][memo[y]] = min(
                d[memo[x]][memo[y]],
                c
            )

        # Use floyd-warshall algorithm to find the
        # minimum distances between any index pairs
        for m in range(n):
            for s in range(n):
                if d[s][m] == float('inf'):
                    continue

                for e in range(n):
                    if d[m][e] == float('inf'):
                        continue

                    d[s][e] = min(
                        d[s][e],
                        d[s][m] + d[m][e]
                    )

        word_lens = set(len(w) for w in original)

        dp = [float('inf')] * (len(target) + 1)
        dp[0] = 0

        for i, y in enumerate(target):
            if dp[i] == float('inf'):
                continue

            x = source[i]
            if x == y:
                dp[i + 1] = min(dp[i + 1], dp[i])

            for l in word_lens:
                if i + l >= len(dp):
                    continue

                sx = source[i: i + l]
                sy = target[i: i + l]
                ix = memo.get(sx, -1)
                iy = memo.get(sy, -1)

                if ix >= 0 and iy >= 0 and d[ix][iy] < float('inf'):
                    dp[i + l] = min(dp[i + l], dp[i] + d[ix][iy])

        if dp[-1] < float('inf'):
            return int(dp[-1])

        return -1
