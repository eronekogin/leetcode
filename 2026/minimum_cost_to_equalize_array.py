"""
https://leetcode.com/problems/minimum-cost-to-equalize-array/description/
"""


class Solution:
    """
    Solution
    """

    def min_cost_to_equalize_array(self, nums: list[int], cost1: int, cost2: int) -> int:
        """
        min cost to equalize array
        """
        r, l = max(nums), min(nums)
        n = len(nums)
        m = 10 ** 9 + 7
        min_increments = r * n - sum(nums)

        # case 1
        if cost1 * 2 <= cost2 or n <= 2:
            return min_increments * cost1 % m

        # case 2:
        # max_diff is r - l, and the remaining is min_increments - max_diff
        # if max_diff > min_increments - max_diff, which makes op1 > 0,
        # we cannot pair all of the increments to use cost2
        op1 = max(0, (r - l) * 2 - min_increments)
        op2 = min_increments - op1
        rslt = (op1 + op2 % 2) * cost1 + op2 // 2 * cost2

        # case 3:
        # when op1 is quite large, it might be cheaper to increase
        # the final array number to be larger than the current max number
        # each time we increase the final max number by 1, we have made
        # new n - 2 pairs since there are n - 2 numbers need also to
        # increase 1
        # So we calculate op1 // (n - 2) to get how many value we need
        # to increase the current max value, and each time we raise
        # the max value, we are actually adding n increments to the
        # min_increments
        min_increments += op1 // (n - 2) * n
        op1 %= (n - 2)
        op2 = min_increments - op1
        rslt = min(
            rslt,
            (op1 + op2 % 2) * cost1 + op2 // 2 * cost2
        )

        # case 4:
        # When cost1 is still too much and we want to see if there is
        # an even cheaper cost to only use cost2, we keep raise the
        # target to make min_increments to an even number and check
        # the result
        # min_increments is odd: if n is odd, loop 1 makes it even, it is best choice
        # min_increments is even: if n is odd: loop 1 still makes it odd,
        # loop 2 makes it even, it is best choice
        for _ in range(2):
            min_increments += n
            rslt = min(
                rslt,
                min_increments % 2 * cost1 + min_increments // 2 * cost2
            )

        return rslt % m
