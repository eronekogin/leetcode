"""
https://leetcode.com/problems/distribute-candies/
"""


from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(candies) >> 1, len(set(candies)))
