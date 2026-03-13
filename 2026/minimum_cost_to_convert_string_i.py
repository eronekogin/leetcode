"""
https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_cost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        """
        minimum cost
        """
        offset = ord('a')
        total_cost = 0

        min_costs = [[float('inf')] * 26 for _ in range(26)]
        for x, y, c in zip(original, changed, cost):
            i, j = ord(x) - offset, ord(y) - offset
            min_costs[i][j] = min(min_costs[i][j], c)

        for m in range(26):
            for s in range(26):
                for e in range(26):
                    min_costs[s][e] = min(
                        min_costs[s][e],
                        min_costs[s][m] + min_costs[m][e]
                    )

        for x, y in zip(source, target):
            if x == y:
                continue

            i, j = ord(x) - offset, ord(y) - offset
            if min_costs[i][j] == float('inf'):
                return -1

            total_cost += min_costs[i][j]

        return int(total_cost)


print(Solution().minimum_cost('abcd', 'acbe', [
      "a", "b", "c", "c", "e", "d"], ["b", "c", "b", "e", "b", "e"], [2, 5, 5, 1, 2, 20]))
