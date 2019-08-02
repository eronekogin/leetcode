"""
https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rslt = [[]]
        for num in nums:
            workRslt = []
            for preRslt in rslt:
                for i in range(len(preRslt) + 1):
                    # Insert the next char to any of the positon of
                    # the pre premutations.
                    workRslt.append(preRslt[:i] + [num] + preRslt[i:])

            rslt = workRslt

        return rslt


nums = [1, 2, 3]
print(Solution().permute(nums))
