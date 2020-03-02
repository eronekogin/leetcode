"""
https://leetcode.com/problems/range-sum-query-immutable/
"""


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums, currSum = [0], 0
        for num in nums:
            currSum += num
            self.sums.append(currSum)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]
