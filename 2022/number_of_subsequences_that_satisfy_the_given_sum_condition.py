"""
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
"""


class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        """
        The order of the subsequence does not matter since for each subsequence
        we only need to find the minimum and maximum number.
        """
        MOD = 10 ** 9 + 7
        sortedNums = sorted(nums)
        cnt = 0
        l, r = 0, len(sortedNums) - 1
        while l <= r:
            if sortedNums[l] + sortedNums[r] > target:
                r -= 1
            else:
                # pow(2, r - l, MOD) is much faster.
                # (1 << (r - l)) % MOD is acceptable but much slower.
                # (2 ** (r - l)) % MOD will result TLE.
                cnt += pow(2, r - l, MOD)
                l += 1

        return cnt % MOD
