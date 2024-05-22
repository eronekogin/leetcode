"""
https://leetcode.com/problems/intersection-of-multiple-arrays/description/
"""


class Solution:
    """
    Solution
    """

    def intersection(self, nums: list[list[int]]) -> list[int]:
        """
        intersection
        """
        rslts = set(nums[0])
        for num in nums:
            rslts &= set(num)

        return sorted(rslts)


print(Solution().intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
