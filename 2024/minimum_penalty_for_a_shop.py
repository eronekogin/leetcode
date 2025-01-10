"""
https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
"""


class Solution:
    """
    Solution
    """

    def best_closing_time(self, customers: str) -> int:
        """
        best closing time
        """
        min_close_time = min_penalty = curr_penalty = 0
        for curr_close_time, is_customer_coming in enumerate(customers):
            if is_customer_coming == 'Y':
                curr_penalty -= 1
            else:
                curr_penalty += 1

            if curr_penalty < min_penalty:
                min_penalty = curr_penalty
                min_close_time = curr_close_time + 1

        return min_close_time
