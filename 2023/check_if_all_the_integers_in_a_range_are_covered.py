"""
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
"""


class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        mergedRanges = []

        for start, end in sorted(ranges):
            if not mergedRanges:
                mergedRanges.append([start, end])
                continue

            if start <= mergedRanges[-1][1] + 1:
                mergedRanges[-1][1] = max(end, mergedRanges[-1][1])
            else:
                mergedRanges.append([start, end])
        
        return any(
            start <= left and end >= right
            for start, end in mergedRanges
        )
    

print(Solution().isCovered([[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]], 15, 38))