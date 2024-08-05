"""
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/
"""


from heapq import heapify, heappop, heappush


class Solution:
    """
    Solution
    """

    def fill_cups(self, amount: list[int]) -> int:
        """
        fill cups
        """
        heap = [-x for x in amount if x > 0]
        heapify(heap)
        seconds = 0
        while len(heap) >= 2:
            m1 = heappop(heap)
            m2 = heappop(heap)
            if m1 < -1:
                heappush(heap, m1 + 1)

            if m2 < -1:
                heappush(heap, m2 + 1)

            seconds += 1

        if heap:
            seconds -= heappop(heap)

        return seconds

    def fill_cups2(self, amount: list[int]) -> int:
        return max(amount + [(sum(amount) + 1) >> 1])
