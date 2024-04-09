"""
https://leetcode.com/problems/divide-array-into-equal-pairs/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def divide_array(self, nums: list[int]) -> bool:
        """
        divide array
        """
        cnt = Counter(nums)
        return all(v & 1 == 0 for v in cnt.values())
