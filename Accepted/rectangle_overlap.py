"""
https://leetcode.com/problems/rectangle-overlap/
"""


class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        # Filter out empty rectangle first.
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or \
                rec2[1] == rec2[3]:
            return False

        # Then check the boarders.
        if rec2[0] >= rec1[2] or rec2[2] <= rec1[0]:
            return False
        else:
            if rec2[1] >= rec1[3] or rec2[3] <= rec1[1]:
                return False
            else:
                return True


print(Solution().isRectangleOverlap([-1, 0, 1, 1],
                                    [0, -1, 0, 1]))
