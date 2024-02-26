"""
https://leetcode.com/problems/minimum-cost-to-set-cooking-time/description/
"""


class Solution:
    """
    Solution
    """

    def min_cost_set_time(
        self, start_at: int,
        move_cost: int, push_cost: int,
        target_seconds: int
    ) -> int:
        """
        min_cost_set_time
        """
        def get_cost(minutes: int, seconds: int):
            if minutes > 99 or seconds > 99 or minutes < 0 or seconds < 0:
                return max_cost

            curr_pos = str(start_at)
            total_cost = 0

            for c in str(minutes * 100 + seconds):
                total_cost += push_cost
                if c != curr_pos:
                    total_cost += move_cost
                    curr_pos = c

            return total_cost

        max_cost = 4 * (move_cost + push_cost) + 1
        minutes, seconds = divmod(target_seconds, 60)
        return min(
            get_cost(minutes, seconds),
            get_cost(minutes - 1, seconds + 60)
        )
