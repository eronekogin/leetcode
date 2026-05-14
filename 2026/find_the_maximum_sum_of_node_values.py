"""
https://leetcode.com/problems/find-the-maximum-sum-of-node-values/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_value_sum(self, nums: list[int], k: int, edges: list[list[int]]) -> int:
        """
        Notice that although one operation can only happen on adjancent nodes u and v,
        but if there is an edge between v and w, then if we apply operations on both
        (u, v) and (v, w), we would have:

        1. (u, v) -> (u ^ k, v ^ k)
        2. (v ^ k, w) -> (v, w ^ k)

        so this equals to that we apply the operation on pair (u, w).

        In this case we can caluate the net_change for each node value x with its
        operated value x ^ k, then:

        1. If the total number of positive net_change nodes are even, we can form them
            into pairs in our final result.

        2. Else, we can check it against the minimum postive net_change and the maximum
            negative net_change.
        """
        node_sum = 0
        positive_net_change_cnt = 0
        positive_min = 1 << 30
        negative_max = -1 * positive_min

        for v in nums:
            node_sum += v
            v1 = v ^ k
            net_change = v1 - v
            if net_change > 0:
                positive_min = min(positive_min, net_change)
                node_sum += net_change
                positive_net_change_cnt += 1
            else:
                negative_max = max(negative_max, net_change)

        if positive_net_change_cnt & 1 == 0:
            # all of them can form complete pairs
            return node_sum

        return max(
            node_sum - positive_min,
            node_sum + negative_max
        )
