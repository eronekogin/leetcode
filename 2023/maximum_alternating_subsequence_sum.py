"""
https://leetcode.com/problems/maximum-alternating-subsequence-sum/
"""


class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        """
        even means the maximum alternating sum ends at an even index.
        odd means the maximum alternating sum ends at an odd index.

        so for the next number, we have:
            odd = max(odd, even - num)
            even = max(even, odd + num)
        """
        odd = even = 0
        for num in nums:
            odd, even = max(odd, even - num), max(even, odd + num)

        return even
