"""
https://leetcode.com/problems/water-bottles-ii/description/
"""


class Solution:
    """
    Solution
    """

    def max_bottles_drunk(self, num_bottles: int, num_exchange: int) -> int:
        """
        max bottles drunk
        """
        rslt = num_bottles
        curr_exchange = num_exchange
        curr_bottles = num_bottles
        while curr_exchange <= curr_bottles:
            rslt += 1
            curr_bottles = curr_bottles - curr_exchange + 1
            curr_exchange += 1

        return rslt
