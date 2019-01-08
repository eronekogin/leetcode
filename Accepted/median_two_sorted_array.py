"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Assumption: nums1 and nums2 must be sorted in ascending order first.
        n1 = len(nums1)
        n2 = len(nums2)
        minNum = float('-inf')
        maxNum = float('inf')

        # Looping on the small array in order to achieve O(log(min(n1, n2))).
        if n1 < n2:
            return self.findMedianSortedArrays(nums2, nums1)

        start = 0
        end = n2 << 1

        """ 
        For a single array with N items, the total possible cut positions
        is 2N + 1. So for two arrays with N1 and N2 items, the total cut
        positions is 2N1 + 2N2 + 2.

        So if we cut the two array into two half with same length, the 
        length is always N1 + N2 as the index is 0 based, and it needs
        2 additional position for the cut poistion in each half.
        """
        while start <= end:
            c2 = (start + end) >> 1  # Try to cut in the middle of nums2
            c1 = n1 + n2 - c2  # Calculate the cut pos in nums1

            if c1 == 0:
                l1 = minNum
            else:
                l1 = nums1[(c1 - 1) >> 1]

            if c2 == 0:
                l2 = minNum
            else:
                l2 = nums2[(c2 - 1) >> 1]

            if c1 == n1 * 2:
                r1 = maxNum
            else:
                r1 = nums1[c1 >> 1]

            if c2 == n2 * 2:
                r2 = maxNum
            else:
                r2 = nums2[c2 >> 1]

            """
            We just need to ensure l1 <= r2 and l2 <= r1 as originally
            nums1 and nums2 are sorted in ascending order, thus l1 <= l2
            and l2 <= r2 are already satisfied.
            """
            if l1 > r2:  # left half in nums1 is too big, move c1 to left
                # c1 to left is the same as c2 to right
                start = c2 + 1
            elif l2 > r1:  # left half in nums2 is too big, move c2 to left
                end = c2 - 1
            else:  # Found the right cut position
                return (max(l1, l2) + min(r1, r2)) / 2

        # When coming here, no result is found.
        return None


nums1 = [3]
nums2 = [-2, -1]
s = Solution()
print(s.findMedianSortedArrays(nums1, nums2))
