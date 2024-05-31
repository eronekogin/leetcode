"""
https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
"""


class Solution:
    """
    Solution
    """

    def minimum_card_pickup(self, cards: list[int]) -> int:
        """
        minimum card pick up
        """
        min_diff = n = len(cards) + 1
        prevs: dict[int, int] = {}
        for i, c in enumerate(cards):
            if c in prevs:
                min_diff = min(min_diff, i - prevs[c] + 1)

            prevs[c] = i

        if min_diff == n:
            return -1

        return min_diff


print(Solution().minimum_card_pickup([3, 4, 2, 3, 4, 7]))
