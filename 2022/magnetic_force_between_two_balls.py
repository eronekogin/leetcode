"""
https://leetcode.com/problems/magnetic-force-between-two-balls/
"""


class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        def count_balls(distance: int) -> int:
            cnt = 1
            start = sortedPositions[0]
            for i in range(1, N):
                if sortedPositions[i] - start >= distance:
                    cnt += 1
                    start = sortedPositions[i]

            return cnt

        sortedPositions = sorted(position)
        N = len(sortedPositions)

        l, r = 0, sortedPositions[-1] - sortedPositions[0]
        while l < r:
            mid = r - ((r - l) >> 1)
            if count_balls(mid) >= m:
                l = mid
            else:
                r = mid - 1

        return l


print(Solution().maxDistance([5, 4, 3, 2, 1, 1000000000],
                             2))
