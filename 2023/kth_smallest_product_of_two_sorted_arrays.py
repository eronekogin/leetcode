"""
https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays/
"""


class Solution:
    """
    Solution
    """

    def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """
        kth_smallest_product
        """
        def count(nums1: list[int], nums2: list[int], x: int):
            """
            Count how many numbers of products from nums1 and nums2 are <= x, both
            nums1 and nums2 are sorted with only non-negative integers.
            """
            cnt = 0
            j = len(nums2) - 1
            for a in nums1:
                while j >= 0 and a * nums2[j] > x:
                    j -= 1

                cnt += j + 1

            return cnt

        a1 = [-x for x in nums1 if x < 0][::-1]
        a2 = [x for x in nums1 if x >= 0]
        b1 = [-y for y in nums2 if y < 0][::-1]
        b2 = [y for y in nums2 if y >= 0]
        total_negative_numbers = len(a1) * len(b2) + len(a2) * len(b1)

        if k > total_negative_numbers:
            k -= total_negative_numbers
            sign = 1
        else:
            k = total_negative_numbers - k + 1
            b1, b2 = b2, b1
            sign = -1

        l, r = 0, 10 ** 10
        while l < r:
            m = ((r - l) >> 1) + l
            if count(a1, b1, m) + count(a2, b2, m) >= k:
                r = m
            else:
                l = m + 1

        return l * sign
