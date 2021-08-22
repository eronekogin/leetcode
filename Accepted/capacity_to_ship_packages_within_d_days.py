"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        """
        Doing binary search on the needed days:
            1. Calculate a possible capacity from the maximum of the weights
                and the sum of the weights.
            2. Then calculate how many days needed based on the current
                capacity.
            3. Then check if capacity is too large or too small based on
                the required days.
        """
        l, r = max(weights), sum(weights)
        while l < r:
            m = l + ((r - l) >> 1)
            currWeight, currDays = 0, 1
            for w in weights:
                if currWeight + w > m:
                    currDays += 1
                    currWeight = 0

                currWeight += w

            if currDays > days:
                l = m + 1
            else:
                r = m

        return l
