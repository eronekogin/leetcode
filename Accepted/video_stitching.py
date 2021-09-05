"""
https://leetcode.com/problems/video-stitching/
"""


class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        preEnd, nextEnd, clipCnt = -1, 0, 0
        for start, end in sorted(clips):
            if nextEnd >= time or start > nextEnd:
                break
            elif preEnd < start <= nextEnd and end > nextEnd:
                clipCnt += 1
                preEnd = nextEnd

            nextEnd = max(nextEnd, end)

        if nextEnd >= time:
            return clipCnt

        return -1
