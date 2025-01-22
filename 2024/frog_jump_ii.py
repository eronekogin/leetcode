"""
https://leetcode.com/problems/frog-jump-ii/description/
"""


class Solution:
    """
    Solution
    """

    def max_jump(self, stones: list[int]) -> int:
        """
        Think about the path as two paths without intersection, which
        means we could think of two frogs to jump from left to right
        and the other jumps from right to left.

        Apparently f1 f2 f1 f2 is better than f1 f2 f2 f1, because in
        the second positions frog1 jumps farther than in the first
        positions.
        """
        min_cost = stones[1] - stones[0]
        for i in range(2, len(stones)):
            min_cost = min(min_cost, stones[i] - stones[i - 2])

        return min_cost
