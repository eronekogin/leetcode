"""
https://leetcode.com/problems/find-number-of-ways-to-reach-the-k-th-stair/description/
"""


from math import comb


class Solution:
    """
    Solution
    """

    def ways_to_reach_stair(self, k: int) -> int:
        """
        1. The go up actions are fixed, suppose alice performed m jumps,
            her total up distance is 1 + 2 + 4 + ... + 2^(m - 1) = 2^m - 1
        2. Since she starts at 1, if she performed m jumps, she will be on the 2^m stair.
        3. So she needs down moves 2^m - k to reach the kth stair.
        4. However she cannot go down consecutively, but can only before the first jump
            between two adjencent jump and after the last jump, since she has m total jumps,
            such slots for down move is m + 1, and we can pick up 2^m - k from m + 1 slots
        """
        rslt = 0

        # Find the smallest jump satisfies 2^jump >= k
        # using k - 1 to handle the case when k is just the power of 2.
        jump = (k - 1).bit_length() if k > 0 else 0

        while True:
            down = (1 << jump) - k
            if down > jump + 1:
                break

            rslt += comb(jump + 1, down)
            jump += 1

        return rslt
