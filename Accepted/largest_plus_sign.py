"""
https://leetcode.com/problems/largest-plus-sign/
"""


from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        """
        Suppose minArms[r][c] stores the minumum length of four arms which are
        expanded from the center (r, c) and goes in four directions.

        Then our answer is to find the maximum value in the minArms in order to
        find the longest arms which could form a plus sign.
        """
        minArms = [[0] * N for _ in range(N)]
        blocked = {(r, c) for r, c in mines}
        rslt = 0
        for r in range(N):
            cnt = 0
            for c in range(N):  # From left to right.
                if (r, c) not in blocked:
                    cnt += 1
                else:
                    cnt = 0

                minArms[r][c] = cnt

            cnt = 0
            for c in reversed(range(N)):  # From right to left.
                if (r, c) not in blocked:
                    cnt += 1
                else:
                    cnt = 0

                minArms[r][c] = min(minArms[r][c], cnt)

        for c in range(N):
            cnt = 0
            for r in range(N):  # From top to bottom.
                if (r, c) not in blocked:
                    cnt += 1
                else:
                    cnt = 0

                minArms[r][c] = min(minArms[r][c], cnt)

            cnt = 0
            for r in reversed(range(N)):  # From bottom to top.
                if (r, c) not in blocked:
                    cnt += 1
                else:
                    cnt = 0

                minArms[r][c] = min(minArms[r][c], cnt)
                rslt = max(rslt, minArms[r][c])

        return rslt


print(Solution().orderOfLargestPlusSign(5, [[4, 2]]))
