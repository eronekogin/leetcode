"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
"""


from collections import deque


class Solution:
    def shortestSubarray(self, A: list[int], K: int) -> int:
        """
        1. The problem could be translated to find the smallest y - x for
            x, y are the indexes of the prefix sum list P, while P[y] - P[x]
            >= K.
            1.1 Notice that P[y] - P[x] stands for the sum for the contiguous
                subarray from x to y - 1, with length y - 1 - x + 1 = y - x.
        2. Then we keep the indexes for all the increasing P[y] in the queue:
            2.1 if x1 < x2 and P[x1] > P[x2], then P[y] - P[x2] < P[y] - P[x1]
                <= K, and y - x2 < y - x1, which means x2 is a better
                candidate than x1, so we don't need to consider x1 any longer.
            2.2 On the other hand, if we could find a y which just has P[y] -
                p[x_0] >= K, then we don't need to consider this x_0 any
                longer as future y must have a longer length than the current
                y.
                2.2.1 The x_0 means the first element in the current queue.
        """
        N = len(A)
        P = [0]

        # First calculate prefix sums for A.
        for x in A:
            P.append(P[-1] + x)

        rslt = N + 1
        queue = deque()
        for y, py in enumerate(P):
            while queue and py <= P[queue[-1]]:
                queue.pop()  # Remove the descreasing previous pi.

            while queue and py - P[queue[0]] >= K:
                # Determine the current minimum length.
                rslt = min(rslt, y - queue.popleft())

            queue.append(y)  # Append the current index to queue.

        if rslt == N + 1:
            return -1

        return rslt


print(Solution().shortestSubarray([1, 2, 1, 4], 5))
