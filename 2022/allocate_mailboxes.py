"""
https://leetcode.com/problems/allocate-mailboxes/
"""


from functools import lru_cache


class Solution:
    def minDistance(self, houses: list[int], k: int) -> int:
        """
        The minimum cost for houses between i to j to its nearest mailbox is
        to put the mailbox at the median of [i: j].
        """
        @lru_cache(None)
        def dp(remainMailBoxes: int, currHouseIndex: int) -> int:
            if remainMailBoxes == 0 and currHouseIndex == N:
                # Completed counting on the last house.
                return 0

            if remainMailBoxes == 0 or currHouseIndex == N:
                # Not possible to distribute.
                return float('inf')

            cost = float('inf')
            for pivot in range(currHouseIndex, N):
                cost = min(
                    cost,
                    minCosts[currHouseIndex][pivot] + dp(
                        remainMailBoxes - 1,
                        pivot + 1
                    )
                )

            return cost

        N = len(houses)

        # Calculate minimum cost between each pair of the house first.
        sortedHouses = sorted(houses)
        minCosts = [[0] * N for _ in range(N)]
        for start in range(N):
            for end in range(N):
                m = sortedHouses[(start + end) >> 1]
                for i in range(start, end + 1):
                    minCosts[start][end] += abs(m - sortedHouses[i])

        return dp(k, 0)
