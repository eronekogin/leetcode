"""
https://leetcode.com/problems/maximum-average-pass-ratio/
"""


from heapq import heappush, heappop


class Solution:
    def maxAverageRatio(
        self,
        classes: list[list[int]],
        extraStudents: int
    ) -> float:
        def nextProfit(x: int, y: int):
            return (x + 1) / (y + 1) - x / y

        heap = []
        totalScore = 0
        for x, y in classes:
            if x == y:
                totalScore += 1
            else:
                heappush(heap, (-nextProfit(x, y), x, y))

        if heap:
            for _ in range(extraStudents):
                _, x, y = heappop(heap)
                heappush(heap, (-nextProfit(x + 1, y + 1), x + 1, y + 1))

            totalScore += sum(x / y for _, x, y in heap)

        return totalScore / len(classes)
