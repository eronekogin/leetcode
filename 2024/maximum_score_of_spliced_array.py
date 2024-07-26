"""
https://leetcode.com/problems/maximum-score-of-spliced-array/description/
"""


class Solution:
    """
    Solution
    """

    def maximums_spliced_array(self, nums1: list[int], nums2: list[int]) -> int:
        """
        maximums spliced array
        """
        def kadane(a: list[int], b: list[int]):
            rslt = curr = 0
            tb = 0

            for x, y in zip(a, b):
                curr = max(0, curr + x - y)
                rslt = max(rslt, curr)
                tb += y

            return rslt + tb

        return max(kadane(nums1, nums2), kadane(nums2, nums1))


print(Solution().maximums_spliced_array(
    [20, 40, 20, 70, 30], [50, 20, 50, 40, 20]))
