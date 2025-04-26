"""
https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/description/
"""


class Solution:
    """
    Solution
    """

    def max_score(self, nums: list[int]) -> int:
        """
        max score
        """
        nums.sort(reverse=True)
        cnt = 0
        curr_sum = 0
        for x in nums:
            curr_sum += x
            if curr_sum > 0:
                cnt += 1
            else:
                break

        return cnt
