"""
https://leetcode.com/problems/minimum-number-of-coins-to-be-added/description/
"""


class Solution:
    """
    Docstring for Solution
    """

    def minimum_added_coins(self, coins: list[int], target: int) -> int:
        """
        suppose current max is 3, which means we can form numbers [0, 1, 2, 3],
        then if we add curr_max + 1, which is 4, we can form numbers
        [0, 1, 2, 3, 4, 5, 6, 7], which pushes the current range to the highest
        place without lost consecutivity
        """
        coins.sort()
        current_max = 0
        additions = 0
        index = 0

        while current_max < target:
            if index < len(coins) and coins[index] <= current_max + 1:
                current_max += coins[index]
                index += 1
            else:
                current_max += current_max + 1
                additions += 1

        return additions
