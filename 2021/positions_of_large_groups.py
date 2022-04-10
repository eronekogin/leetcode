"""
https://leetcode.com/problems/positions-of-large-groups/
"""


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        rslt = []
        start = 0
        for end, c in enumerate(s + ' '):
            if c != s[end - 1]:
                if end - start >= 3:
                    rslt.append([start, end - 1])

                start = end

        return rslt


print(Solution().largeGroupPositions("abbxxxxzzy"))
