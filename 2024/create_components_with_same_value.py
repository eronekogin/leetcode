"""
https://leetcode.com/problems/create-components-with-same-value/description/
"""


class Solution:
    """
    Solution
    """

    def component_value(self, nums: list[int], edges: list[list[int]]) -> int:
        """
        component value
        """
        def post_order(curr_node: int, parent_node: int):
            rslt = nums[curr_node]

            for next_node in tree[curr_node]:
                if next_node != parent_node:
                    rslt += post_order(next_node, curr_node)

            if rslt == part_sum:
                return 0

            return rslt

        tree = [[] for _ in nums]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        total = sum(nums)
        for part_sum in range(1, (total >> 1) + 1):
            if total % part_sum == 0 and post_order(0, -1) == 0:
                return total // part_sum - 1

        return 0
