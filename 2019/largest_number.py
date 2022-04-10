"""
https://leetcode.com/problems/largest-number/
"""


from typing import List


class CompareKey(str):
    def __lt__(self, other: 'CompareKey') -> bool:
        """
        Add customized comparison operations for less than, so that
        '3' + '30' = '330' > '30' + '3' = '303', then '3' will be 
        preceding '30' when sort in descending order.
        """
        return self + other > other + self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        rslt = ''.join(sorted(map(str, nums), key=CompareKey))
        if rslt[0] == '0':
            return '0'

        return rslt


nums = [10, 2]
print(Solution().largestNumber(nums))
