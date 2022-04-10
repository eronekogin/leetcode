"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""


from typing import List

from collections import deque


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        """
        Simple BFS.
        """
        if N < 1 or K < 0:
            return []

        if N == 1:
            return [i for i in range(10)]

        queue = deque((1, i) for i in range(1, 10))
        rslt = []
        while queue:
            digitCnt, currNum = queue.popleft()
            if digitCnt == N:
                rslt.append(currNum)
            else:
                lastDigit = currNum % 10
                queue.extend(
                    (digitCnt + 1, currNum * 10 + nextDigit)
                    for nextDigit in {lastDigit + K, lastDigit - K}
                    if 0 <= nextDigit <= 9)

        return rslt


print(Solution().numsSameConsecDiff(3, 1))
