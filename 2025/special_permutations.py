"""
https://leetcode.com/problems/special-permutations/description/
"""


from functools import cache


class Solution:
    """
    Solution
    """

    def special_perm(self, nums: list[int]) -> int:
        """
        special perm
        """
        @cache
        def dfs(prev: int, mask: int) -> int:
            if mask == (1 << n) - 1:
                return 1

            cnt = 0
            for i in range(n):
                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    cnt += dfs(nums[i], mask | (1 << i))

            return cnt % m

        n = len(nums)
        m = 10 ** 9 + 7
        return dfs(1, 0)
