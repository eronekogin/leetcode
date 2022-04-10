"""
https://leetcode.com/problems/find-median-from-data-stream/


For ideas on the follow up questions, see https://leetcode.com/problems/find-median-from-data-stream/discuss/343662/JAVA-HEAP-SOLUTION-%2B-2-FOLLOW-UPS
for more details.
"""


from heapq import heappush, heappop, heappushpop


class MedianFinder:

    def __init__(self):
        self.heaps = ([], [])

    def addNum(self, num: int):
        """
        lows holds the smaller half of the numbers while highs holds the larger
        half.

        1. Add the input number to the highs first then pop the current
            smallest number in the highs.

        2. Add the negate of the above popped number to the lows, so that lows
            could determine where its position will be.

        3. If highs contains less numbers than lows, pop the current smallest
            number in lows (which will be the largest number in the current
            lower half of the numbers), then add its negate to the highs.
        """
        lows, highs = self.heaps
        heappush(lows, -heappushpop(highs, num))
        if len(highs) < len(lows):
            heappush(highs, -heappop(lows))

    def findMedian(self) -> float:
        """
        1. If highs contain more numbers than lows, it means the current total
            number is 2k + 1, so the median is stored at highs[0].

        2. If highs and lows contain the same numbers, it means the current
            total number is 2k, so the median is between the two top numbers
            on highs and lows.
        """
        lows, highs = self.heaps
        if len(highs) > len(lows):
            return float(highs[0])

        return (highs[0] - lows[0]) / 2
