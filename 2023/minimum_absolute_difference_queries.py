"""
https://leetcode.com/problems/minimum-absolute-difference-queries/
"""


class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        N = max(nums)
        freqs = [[0] * (N + 1)]

        # Canculate frequency of number at each position.
        for num in nums:
            freqs.append(freqs[-1][:])
            freqs[-1][num] += 1
        
        rslt = []
        for l, r in queries:
            diff = [i for i in range(N + 1) if freqs[l][i] != freqs[r + 1][i]]
            rslt.append(
                min(
                    [b - a for a, b in zip(diff, diff[1:])],
                    default=-1
                )
            )
        
        return rslt

