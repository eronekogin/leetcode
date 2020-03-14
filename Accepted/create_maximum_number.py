"""
https://leetcode.com/problems/create-maximum-number/
"""


from typing import List


class Solution:
    def maxNumber(
            self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def get_single_max(nums: List[int], k: int) -> List[int]:
            """
            Take [49321876] for an example:
            k=7 -> dropCnt=1 -> drop 4 -> max=[9321876].
            k=6 -> drop 1 from the above max -> drop 1 -> max=[932876].
            k=5 -> drop 1 from the above max -> drop 2 -> max=[93876].
            k=4 -> drop 1 from the above max -> drop 3 -> max=[9876].
            Since now 9876 is a list in descending order, for smaller k, we
            simply get max[:k] without additional checking.
            """
            if not k:  # Drop all.
                return []

            dropCnt, rslt = len(nums) - k, []
            if not dropCnt:  # Nothing to drop.
                return nums[:]

            for num in nums:
                while dropCnt and rslt and rslt[-1] < num:
                    rslt.pop()
                    dropCnt -= 1

                rslt.append(num)

            return rslt[:k]  # Return the first k digits.

        def merge(a: List[int], b: List[int]) -> List[int]:
            """
            Merge a and b so that they could form the final
            maximum number list.
            """
            return [max(a, b).pop(0) for _ in a + b]

        """
        Now the problem becomes to find the maximum combinations from nums1
        and nums2.
        """
        n1, n2 = len(nums1), len(nums2)
        rslt = []
        for i in range(k + 1):
            if i <= n1 and k - i <= n2:
                rslt = max(rslt, merge(
                    get_single_max(nums1, i), get_single_max(nums2, k - i)))

        return rslt


nums1 = [8, 6, 9]
nums2 = [1, 7, 5]
k = 3
print(Solution().maxNumber(nums1, nums2, k))
