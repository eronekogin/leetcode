"""
https://leetcode.com/problems/ant-on-the-boundary/description/
"""


class Solution:
    """
    Solution
    """

    def return_to_boundary_count(self, nums: list[int]) -> int:
        """
        return to boundary count
        """
        curr = 0
        cnt = 0
        for x in nums:
            curr += x
            if curr:
                continue

            cnt += 1

        return cnt
