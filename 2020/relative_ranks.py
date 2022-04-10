"""
https://leetcode.com/problems/relative-ranks/
"""


from typing import List


class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        """
        Presumption: Each number in the input list is unique.
        """
        sortedNums = reversed(sorted(nums))
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        ranks += [str(i) for i in range(4, len(nums) + 1)]
        return list(map(dict(zip(sortedNums, ranks)).get, nums))
