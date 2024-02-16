"""
https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/description/
"""


class Solution:
    """
    Solution
    """

    def count_elements(self, nums: list[int]) -> int:
        """
        count_elements
        """
        if len(nums) < 3:
            return 0

        sorted_nums = sorted(nums)
        n = len(nums) - 1
        start = n
        for i in range(1, n):
            if sorted_nums[i] > sorted_nums[i - 1]:
                start = i
                break

        end = 0
        for i in range(n - 1, 0, -1):
            if sorted_nums[i] < sorted_nums[i + 1]:
                end = i
                break

        return max(0, end - start + 1)


print(Solution().count_elements([-100000, -99999, -99999]))
