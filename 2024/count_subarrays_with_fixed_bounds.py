"""
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
"""


class Solution:
    """
    Solution
    """

    def count_subarrays(self, nums: list[int], mink: int, maxk: int) -> int:
        """
        count subarrays
        """
        cnt = 0
        jmin = jmax = jbad = -1

        for i, x in enumerate(nums):
            if x < mink or x > maxk:
                jbad = i

            if x == mink:
                jmin = i

            if x == maxk:
                jmax = i

            cnt += max(0, min(jmax, jmin) - jbad)

        return cnt
