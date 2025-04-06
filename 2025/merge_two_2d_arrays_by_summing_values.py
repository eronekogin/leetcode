"""
https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
"""


class Solution:
    """
    Solution
    """

    def merge_arrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        """
        merge arrays
        """
        i1 = i2 = 0
        n1, n2 = len(nums1), len(nums2)
        rslt: list[list[int]] = []
        while i1 < n1 and i2 < n2:
            if nums1[i1][0] == nums2[i2][0]:
                rslt.append([nums1[i1][0], nums1[i1][1] + nums2[i2][1]])
                i1 += 1
                i2 += 1
            elif nums1[i1][0] < nums2[i2][0]:
                rslt.append(nums1[i1])
                i1 += 1
            else:
                rslt.append(nums2[i2])
                i2 += 1

        if i1 < n1:
            rslt.extend(nums1[i1:])

        if i2 < n2:
            rslt.extend(nums2[i2:])

        return rslt


print(Solution().merge_arrays(
    [[2, 4], [3, 6], [5, 5]], [[1, 3], [4, 3]]))
