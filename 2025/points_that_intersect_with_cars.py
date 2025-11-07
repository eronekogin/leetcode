"""
https://leetcode.com/problems/points-that-intersect-with-cars/description/
"""


class Solution:
    """
    Solution
    """

    def number_of_points(self, nums: list[list[int]]) -> int:
        """
        sort
        """
        nums.sort()
        x0, y0 = nums[0]
        rslt = 0
        for x, y in nums:
            if x <= y0:
                y0 = max(y0, y)
                continue

            rslt += y0 - x0 + 1
            x0, y0 = x, y

        return rslt + y0 - x0 + 1

    def number_of_points_2(self, nums: list[list[int]]) -> int:
        """
        line swap
        """
        max_end = max(y for _, y in nums) + 2
        lines: list[int] = [0] * max_end
        for start, end in nums:
            lines[start] += 1
            lines[end + 1] -= 1

        rslt = 0
        for i in range(1, max_end):
            lines[i] += lines[i - 1]
            rslt += (lines[i] > 0)

        return rslt


print(Solution().number_of_points_2([[3, 6], [1, 5], [4, 7]]))
