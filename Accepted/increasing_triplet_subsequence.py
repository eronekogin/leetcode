"""
https://leetcode.com/problems/increasing-triplet-subsequence/
"""


from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True  # Found an increasing triplet.

        return False
