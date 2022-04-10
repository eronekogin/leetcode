"""
https://leetcode.com/problems/set-intersection-size-at-least-two/
"""


from typing import List


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        1. The minimum intersect is selected based on all the intervals, so it
            does not have any relationship on the order of the intervals.
        2. Then we could sort the given input intervals by its end point in
            ascending order first, then by its start point in descending order
            as we would like to process the small intervals first.
        3. If we check the different minimum intersect from different subarry
            of the sorted intervals, we could find that the size of such
            minimum intersects are non-decreasing. In other words, if we have
            more intervals, the size of the minimum intersect either stay the
            same or become larger.
        4. So in order to find the min_size(intervals[0:n - 1]), we need to
            first find the min_size(intervals[0: n - 2]) and so on.
        5. Then we have three cases to determine each time we process a new
            interval:
            5.1 The current interval is full overlapping with the previous one.
            5.2 The current interval is not overlapping with the previous one.
            5.3 The current interval is overlapping with the previous one in
                the middle part.
        6. Each time we keep monitoring the largest and the second largest
            number from the previous minimum intersect, then use them to
            compare with the new interval for the above cases.
        """
        minSize = 0
        preMax, preSecondMax = -1, -2
        for start, end in sorted(intervals, key=lambda x: (x[1], -x[0])):
            if preMax < start:  # No overlap.
                minSize += 2
                preMax, preSecondMax = end, end - 1
            elif preSecondMax >= start:  # Full overlap.
                pass
            else:  # Overlap in the middle.
                minSize += 1
                preMax, preSecondMax = end, preMax

        return minSize
