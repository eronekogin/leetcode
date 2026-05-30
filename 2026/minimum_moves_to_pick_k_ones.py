"""
https://leetcode.com/problems/minimum-moves-to-pick-k-ones/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def minimum_moves(self, nums: list[int], k: int, max_changes: int) -> int:
        """
        1. create stragety takes 2 moves
        2. swap strategy takes d moves where d is the distance between the
            target index to where alice stands. Notice that two adjancent ones
            does not block the swap, take it as a step stone so we keep
            swapping on the other 1 instead but the total cost would still be
            d
        """
        ones = [i for i, x in enumerate(nums) if x == 1]
        n = len(ones)
        p = [0] + list(accumulate(ones))

        # minmum ones we need to pick up from
        # existing ones instead of creating
        m = max(0, k - max_changes)

        # Alice can only pick at most k ones
        # Alice cannot pick more than n existing ones
        # for any ones having a distance less than 3 to where
        # alice stands, it would take less than 3 moves to complete,
        # which would cost the same or less than the create strategy
        # but when it comes to a distance more than 3, alice won't choose
        # to grab that existing one since she can choose the create strategy
        # for this one to get lower cost.
        max_pick_ones = min(n, m + 3, k)
        rslt = float('inf')

        for j in range(m, max_pick_ones + 1):
            # sliding window with a size j and alice should always stands
            # in the median of this window. then in order to calculate
            # the distance of each point in this window to j, we have:
            # sum(right - median) + sum(median - left) = sum(right) - sum(left)
            for i in range(n - j + 1):
                left_sum = p[i + j // 2] - p[i]
                right_sum = p[i + j] - p[i + j - j // 2]

                # add the cost from the remaining ones using create
                # strategy
                rslt = min(rslt, right_sum - left_sum + (k - j) * 2)

        return int(rslt)
