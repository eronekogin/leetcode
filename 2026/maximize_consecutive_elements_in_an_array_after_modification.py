"""
https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def max_selected_elements(self, nums: list[int]) -> int:
        """
        dp[x] stands for the maximum length of
        consecutive sequences ends at x
        """
        nums.sort()
        dp = defaultdict(int)
        for x in nums:
            dp[x + 1] = dp[x] + 1
            dp[x] = dp[x - 1] + 1

        return max(dp.values())

    def max_selected_elements_2(self, nums: list[int]) -> int:
        """
        O(1) space solution

        c1 stands for the max len of consecutive sequences ends at x
        c2 stands for the max len of consecutive sequences ends at x + 1
        """
        nums.sort()
        prev = -2  # Ensure prev + 2 <= 0
        rslt = c1 = c2 = 1
        for x in nums:
            if x == prev:
                c2 = c1 + 1
            elif x == prev + 1:
                c1, c2 = c1 + 1, c2 + 1
            elif x == prev + 2:
                c1, c2 = c2 + 1, 1
            else:
                c1 = c2 = 1

            rslt = max(rslt, c1, c2)
            prev = x

        return rslt
