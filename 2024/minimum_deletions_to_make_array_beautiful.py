"""
https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/description/
"""


class Solution:
    """
    Solution
    """

    def min_deletion(self, nums: list[int]) -> int:
        """
        min deletion
        """
        deletes = 0
        i, n = 0, len(nums)
        while i < n:
            end = i
            while end + 1 < n and nums[end + 1] == nums[i]:
                end += 1

            deletes += end - i
            i = end + 2

        # Delete the last item if the total length is not even.
        return deletes + ((len(nums) - deletes) & 1)


print(Solution().min_deletion([1, 1, 2, 3, 5]))
