"""
https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/description/
"""


from math import lcm


class Solution:
    """
    Solution
    """

    def minimize_set(
        self,
        divisor1: int,
        divisor2: int,
        unique_cnt1: int,
        unique_cnt2: int
    ) -> int:
        """
        Suppose L is our candidate maximum value, then from range [1, L], we have:

        * L - multiple of divisor1 should >= unique_cnt1
        * L - multiple of divisor2 should >= unique_cnt2
        * L - multiple of lcm(divisor1, divisor2) should >= unique_cnt1 + unique_cnt2
        """
        l, r = 0, 10 ** 10
        g = lcm(divisor1, divisor2)
        min_required = unique_cnt1 + unique_cnt2

        while l < r:
            m = l + ((r - l) >> 1)

            c1 = (m - (m // divisor1)) >= unique_cnt1
            c2 = (m - (m // divisor2)) >= unique_cnt2
            c3 = (m - (m // g)) >= min_required

            if c1 and c2 and c3:
                r = m
            else:
                l = m + 1

        return l
