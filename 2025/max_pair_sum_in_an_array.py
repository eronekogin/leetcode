"""
https://leetcode.com/problems/max-pair-sum-in-an-array/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def max_sum(self, nums: list[int]) -> int:
        """
        max sum
        """
        def get_max_digit(x: int) -> int:
            max_digit = -1
            while x:
                x, r = divmod(x, 10)
                max_digit = max(max_digit, r)

            return max_digit

        memo = defaultdict(list)
        for x in nums:
            memo[get_max_digit(x)].append(x)

        rslt = -1
        for v in memo.values():
            if len(v) >= 2:
                rslt = max(rslt, sum(sorted(v)[-2:]))

        return rslt
