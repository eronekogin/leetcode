"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
"""


from bisect import bisect_left


class Solution:
    def maxValue(self, events: list[list[int]], k: int) -> int:
        """
        Find the maximum value we can get before this meeting starts.

        Repeatly doing this K times.
        """
        sortedEvents = sorted(events, key=lambda x: x[1])
        prev, curr = [[0, 0]], [[0, 0]]
        for _ in range(k):
            for start, end, value in sortedEvents:
                j = bisect_left(prev, [start]) - 1
                if prev[j][1] + value > curr[-1][1]:
                    curr.append([end, prev[j][1] + value])

            prev, curr = curr, [[0, 0]]

        return prev[-1][-1]
