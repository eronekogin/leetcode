"""
https://leetcode.com/problems/maximum-xor-score-subarray-queries/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """
    def maximum_subarray_xor(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        maximum subarray xor
        """
        memo = defaultdict(list)
        for i, j in queries:
            memo[j - i].append((i, j))

        # curr[i] stands for the maximum xor found in any subarray starting at index i
        curr = list(nums)

        rslt: dict[tuple[int, int], int] = {}
        n = len(nums)

        for v in range(n):  # iterate possible subarray length
            for i, j in memo[v]:
                rslt[(i, j)] = curr[i]

            for i in range(n - v - 1):
                nums[i] ^= nums[i + 1]
                curr[i] = max(curr[i], curr[i + 1], nums[i])

        return [rslt[(i, j)] for i, j in queries]
