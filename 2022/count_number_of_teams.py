"""
https://leetcode.com/problems/count-number-of-teams/
"""


class Solution:
    def numTeams(self, rating: list[int]) -> int:
        cnt = 0
        for i, pivot in enumerate(rating):
            lgc = rlc = 0  # LeftGreaterCnt, rightLessCnt
            llc = rgc = 0  # LeftLessCnt, rightGreaterCnt

            # Count left.
            for left in rating[:i]:
                if left > pivot:
                    lgc += 1
                elif left < pivot:
                    llc += 1

            # Count right.
            for right in rating[i + 1:]:
                if right > pivot:
                    rgc += 1
                elif right < pivot:
                    rlc += 1

            """
            For combination with middle number as pivot:
                1. If ascending, its left has llc number of ratings to pick
                    while its right has rgc number of ratings to pick.
                2. If descending, its left has lgc number of ratings to pick
                    while its left has rlc number of ratings to pick.
            """
            cnt += llc * rgc + lgc * rlc

        return cnt


print(Solution().numTeams())
