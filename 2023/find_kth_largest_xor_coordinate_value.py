"""
https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
"""


from heapq import heappush, heappop


class Solution:
    def kthLargestValue(self, matrix: list[list[int]], k: int) -> int:
        R, C = map(len, (matrix, matrix[0]))
        ans = [[0] * (C + 1) for _ in range(R + 1)]
        heap = []
        for r, row in enumerate(matrix):
            for c, cell in enumerate(row):
                ans[r + 1][c + 1] = (
                    cell ^
                    ans[r + 1][c] ^
                    ans[r][c + 1] ^
                    ans[r][c]
                )
                heappush(heap, ans[r + 1][c + 1])
                if len(heap) > k:
                    heappop(heap)

        return heap[0]


print(Solution().kthLargestValue([[5, 2], [1, 6]], 4))
