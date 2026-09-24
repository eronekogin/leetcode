"""
https://leetcode.com/problems/minimum-array-changes-to-make-differences-equal/description/
"""


class Solution:
    """
    Solution
    """

    def min_changes(self, nums: list[int], k: int) -> int:
        """
        min changes
        """
        n = len(nums)
        changes = [0] * (k + 2)

        for i in range(n >> 1):
            l, r = nums[i], nums[n - 1 - i]
            curr_diff = abs(l - r)
            max_diff = max(l, r, k - l, k - r)

            changes[0] += 1  # 0 < diff < curr_diff, need 1 change
            changes[curr_diff] -= 1  # diff == curr_diff, need 0 change
            # curr_diff < diff < max_diff, need 1 change
            changes[curr_diff + 1] += 1
            changes[max_diff + 1] += 1  # diff > max_diff, need 2 changes

        curr_changes = 0
        min_changes = n
        for i in range(k + 1):
            curr_changes += changes[i]
            min_changes = min(min_changes, curr_changes)

        return min_changes
