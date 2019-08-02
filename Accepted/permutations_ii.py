"""
https://leetcode.com/problems/permutations-ii/
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Insert to next number to any of the position of the pre permutations.

        When the next number is found in the pre permutation, skip the loop on
        the current permutation.

        For [1, 1], if we want to insert 1, we will insert the new 1 to the
        left side of the first 1, thus become [1, 1, 1]. Then skip the
        remaining insert positions.
        """
        rslt = [[]]
        for num in nums:
            workRslt = []
            for preRslt in rslt:
                # Add the current number to the end of the preRslt to
                # prevent the not found in the index function. When
                # the pre permutation does not contain the current number,
                # then it is correct to insert the current number to every
                # position of the pre permutation.
                validMaxPos = (preRslt + [num]).index(num)
                for i in range(validMaxPos + 1):
                    workRslt.append(preRslt[:i] + [num] + preRslt[i:])

            rslt = workRslt

        return rslt


nums = [1, 1, 3]
print(Solution().permuteUnique(nums))
