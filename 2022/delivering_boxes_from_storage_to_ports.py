"""
https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/
"""


class Solution:
    def boxDelivering(
        self,
        boxes: list[list[int]],
        portsCount: int,
        maxBoxes: int,
        maxWeight: int
    ) -> int:
        N = len(boxes)
        tripCnt = end = lastEnd = 0
        remainBoxes, remainWeight = maxBoxes, maxWeight
        dp = [0] + [float('inf')] * N
        for start in range(N):
            # Keep loading boxes until reaching limit.
            while end < N and remainBoxes > 0 and remainWeight >= boxes[end][1]:
                remainBoxes -= 1
                remainWeight -= boxes[end][1]
                if end == 0 or boxes[end][0] != boxes[end - 1][0]:
                    lastEnd = end
                    tripCnt += 1

                end += 1

            dp[end] = min(dp[end], dp[start] + tripCnt + 1)

            dp[lastEnd] = min(dp[lastEnd], dp[start] + tripCnt)

            remainBoxes += 1
            remainWeight += boxes[start][1]

            if start == N - 1 or boxes[start][0] != boxes[start + 1][0]:
                tripCnt -= 1

        return dp[-1]


print(Solution().boxDelivering(boxes=[[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]],
                               portsCount=3,
                               maxBoxes=3,
                               maxWeight=6))
