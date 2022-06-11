"""
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/
"""


from heapq import heappush, heappop


class Solution:
    def kthSmallest(self, mat: list[list[int]], k: int) -> int:
        """
        1. Find the k smallest pair sum between two lists which are sorted in
            non-decreasing order.
        2. Then merge each two rows from the matrix until the last one.
        """
        def kSmallestPairSums(
            nums1: list[int],
            nums2: list[int],
            k: int
        ) -> list[list[int]]:
            sumHeap = []
            N1, N2 = len(nums1), len(nums2)

            def push(r: int, c: int) -> None:
                if r < N1 and c < N2:
                    heappush(sumHeap, (nums1[r] + nums2[c], r, c))

            pairSums: list[int] = []
            push(0, 0)
            while sumHeap and len(pairSums) < k:
                pariSum, r, c = heappop(sumHeap)
                pairSums.append(pariSum)
                push(r, c + 1)
                if not c:
                    push(r + 1, c)

            return pairSums

        pairSums = mat[0]
        for i in range(1, len(mat)):
            pairSums = kSmallestPairSums(pairSums, mat[i], k)

        return pairSums[-1]
