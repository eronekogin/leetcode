"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        min operations
        """
        if k == 0:
            if nums1 != nums2:
                return -1

            return 0

        balance = ops = 0

        for a, b in zip(nums1, nums2):
            diff = a - b
            if diff % k != 0:
                return -1

            balance += diff
            if diff > 0:
                ops += diff // k

        if balance == 0:
            return ops

        return -1


print(Solution().min_operations([4, 3, 1, 4], [1, 3, 7, 1], 3))
