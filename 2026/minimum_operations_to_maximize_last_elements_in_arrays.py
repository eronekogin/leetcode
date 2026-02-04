"""
https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def min_operations(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Docstring for min_operations

        :param self: Description
        :param nums1: Description
        :type nums1: list[int]
        :param nums2: Description
        :type nums2: list[int]
        :return: Description
        :rtype: int
        """
        def get_swaps(m1: int, m2: int) -> int:
            swaps = 0
            for a, b in zip(nums1, nums2):
                if a <= m1 and b <= m2:
                    continue

                if a <= m2 and b <= m1:
                    swaps += 1
                else:
                    return -1

            return swaps

        s1 = get_swaps(nums1[-1], nums2[-1])
        s2 = get_swaps(nums2[-1], nums1[-1])
        if s1 == -1 and s2 == -1:
            return -1

        return min(s1, s2)


print(Solution().min_operations([1, 2, 7], [4, 5, 3]))
