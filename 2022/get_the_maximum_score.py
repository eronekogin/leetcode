"""
https://leetcode.com/problems/get-the-maximum-score/
"""


class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:
        """
        Always move the smaller one so we guarantee we encounter
        every "bridge" (arr[i] == arr[j]), if you have [2, 4], and [4,6] and
        you move the pointer on the second array, you won't see the two 4s 
        at the same time.

        When you encounter this "bridge", you basically decide which side 
        (left or right) you should have taken in the previous section - 
        this problem can be seen as you break it up by the elements present 
        in both arrays, then decide which of the sections in between to take.
        """
        i1, i2, n1, n2 = 0, 0, len(nums1), len(nums2)
        preSum1 = preSum2 = 0
        while i1 < n1 or i2 < n2:
            if i1 < n1 and (i2 == n2 or nums1[i1] < nums2[i2]):
                preSum1 += nums1[i1]
                i1 += 1
            elif i2 < n2 and (i1 == n1 or nums2[i2] < nums1[i1]):
                preSum2 += nums2[i2]
                i2 += 1
            else:
                preSum1 = preSum2 = max(preSum1, preSum2) + nums1[i1]
                i1 += 1
                i2 += 1

        return max(preSum1, preSum2) % (10 ** 9 + 7)
