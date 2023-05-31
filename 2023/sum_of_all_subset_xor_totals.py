"""
https://leetcode.com/problems/sum-of-all-subset-xor-totals/
"""


from itertools import combinations
from functools import reduce
import operator


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        total = 0
        for size in range(1, len(nums) + 1):
            for k in combinations(nums, size):
                total += reduce(operator.xor, k)

        return total

    def subsetXORSum2(self, nums: list[int]) -> int:
        """
        consider ith bit for the final result. If there is no element whose ith bit is 1, then all xor subset 
        sums has 0 in ith bit; if there are k (k>=1) elements whose ith bits are 1, then there are in total 
        comb(k, 1) + comb(k,3) + .. = 2**(k-1) ways to select odd number our of these k elements to make the subset
        xor sum's ith bit to be 1, and there are 2**(n-k) ways to choose from the remaining elements whose ith bits
        are 0s. Therefore, we have in total 2**(k-1) * 2**(n-k) = 2**(n-1) subsets whose xor sums have 1 in their
        ith bit, which means the contribution to the final sum is 2**(n-1) * 2**i. Notice this result is irrelevant
        to k. 

        So we only need to determine whether there is any element whose ith bit is 1. We use bitwise OR sum to do this.
        """
        bits = reduce(operator.or_, nums)
        return bits * (1 << (len(nums) - 1))
