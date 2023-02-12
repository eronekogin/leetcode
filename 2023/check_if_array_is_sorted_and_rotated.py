"""
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
"""


class Solution:
    def check(self, nums: list[int]) -> bool:
        i, n = 0, len(nums)
        while i + 1 < n and nums[i + 1] >= nums[i]:
            i += 1

        if i == n - 1:  # already non-decreasing.
            return True

        j = i + 1
        while j + 1 < n:
            if nums[j + 1] >= nums[j]:
                j += 1
            else:  # The suffix is not non-decreasing.
                return False

        if nums[0] < nums[-1]:  # min(prefix) should be >= max(suffix)
            return False

        return True


print(Solution().check([2, 1, 3, 4]))
