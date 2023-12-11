"""
https://leetcode.com/problems/time-needed-to-buy-tickets/
"""


class Solution:
    """
    Solution
    """

    def time_required_to_buy(self, tickets: list[int], k: int) -> int:
        """
        time_required_to_buy
        """
        return sum(
            min(x, tickets[k] if i <= k else tickets[k] - 1)
            for i, x in enumerate(tickets)
        )


print(Solution().time_required_to_buy([2, 3, 2], 2))
