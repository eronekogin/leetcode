"""
https://leetcode.com/problems/optimal-division/
"""


from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        """
        Consider a sequence [a, b, c, d], then rslt is a / min(b, c, d). Then
        for a sequence [b, c, d], we could have b/c/d or b/(c/d), then we have
        b/cd vs bd/c -> 1/d vs d. For any d > 1, 1/d < d, so b/c/d always
        generates the smallest result for a given sequence [b, c, d].
        """
        n = len(nums)
        if n == 1:
            return str(nums[0])

        if n == 2:
            return '/'.join(map(str, nums))

        return '{0}/({1})'.format(nums[0], '/'.join(map(str, nums[1:])))
