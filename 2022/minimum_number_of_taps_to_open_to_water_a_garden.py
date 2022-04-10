"""
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
"""


class Solution:
    """
    Same as https://leetcode.com/problems/video-stitching/
    """

    def minTaps(self, n: int, ranges: list[int]) -> int:
        sortedIntervals = sorted(
            [max(0, i - num), i + num]
            for i, num in enumerate(ranges)
        )

        # Scan intervals.
        preEnd, nextEnd, tapCnt = -1, 0, 0
        for start, end in sortedIntervals:
            if nextEnd >= n or start > nextEnd:
                break
            elif preEnd < start <= nextEnd and end > nextEnd:
                tapCnt += 1
                preEnd = nextEnd

            nextEnd = max(nextEnd, end)

        if nextEnd >= n:
            return tapCnt

        return -1


print(Solution().minTaps(5,
                         [3, 4, 1, 1, 0, 0]))
