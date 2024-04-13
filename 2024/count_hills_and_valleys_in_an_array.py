"""
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/
"""


class Solution:
    """
    Solution
    """

    def count_hill_valley(self, nums: list[int]) -> int:
        """
        count hill valley
        """
        remove_dups: list[int] = []
        i, n = 0, len(nums)
        while i < n:
            while i + 1 < n and nums[i] == nums[i + 1]:
                i += 1

            remove_dups.append(nums[i])
            i += 1

        return sum(
            [
                (remove_dups[i - 1] < remove_dups[i] > remove_dups[i + 1]) or
                (remove_dups[i - 1] > remove_dups[i] < remove_dups[i + 1])
                for i in range(1, len(remove_dups) - 1)
            ] or [0]
        )
