"""
https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_bags(self, capacity: list[int], rocks: list[int], additional_rocks: int) -> int:
        """
        maximum bags
        """
        requires = sorted(y - x for x, y in zip(rocks, capacity))
        cnt = 0
        curr = 0
        for require_rocks in requires:
            if curr + require_rocks > additional_rocks:
                return cnt

            cnt += 1
            curr += require_rocks

        return cnt
