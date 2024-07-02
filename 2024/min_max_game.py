"""
https://leetcode.com/problems/min-max-game/description/
"""


class Solution:
    """
    Solution
    """

    def min_max_game(self, nums: list[int]) -> int:
        """
        min max game
        """
        curr_nums = nums
        is_min = True

        while len(curr_nums) > 1:
            next_nums: list[int] = []
            for i in range(0, len(curr_nums), 2):
                compare = min if is_min else max
                next_nums.append(
                    compare(curr_nums[i], curr_nums[i + 1])
                )

                is_min = not is_min

            curr_nums = next_nums

        return curr_nums.pop()
