"""
https://leetcode.com/problems/maximum-building-height/
"""


class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:
        if not restrictions:
            return n - 1

        maxHeights = [[1, 0]] + restrictions + [[n, n - 1]]
        maxHeights.sort()
        N = len(maxHeights)

        # From left to right.
        for i in range(1, N):
            maxHeights[i][1] = min(
                maxHeights[i][1],
                maxHeights[i - 1][1] + maxHeights[i][0] - maxHeights[i - 1][0]
            )

        # From right to left.
        for i in range(N - 2, -1, -1):
            maxHeights[i][1] = min(
                maxHeights[i][1],
                maxHeights[i + 1][1] + maxHeights[i + 1][0] - maxHeights[i][0]
            )

        maxHeight = 0
        for i in range(1, N):
            l, h1 = maxHeights[i - 1]
            r, h2 = maxHeights[i]
            maxHeight = max(
                maxHeight,
                max(h1, h2) + (r - l - abs(h1 - h2)) // 2
            )

        return maxHeight


print(Solution().maxBuilding(10, [[5, 3], [2, 5], [7, 4], [10, 3]]))
