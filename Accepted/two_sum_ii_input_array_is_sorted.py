"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""


from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i, num in enumerate(numbers):
            chkNum = target - num
            if chkNum in memo:
                return [memo[chkNum] + 1, i + 1]

            memo[num] = i
