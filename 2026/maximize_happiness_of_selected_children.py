"""
https://leetcode.com/problems/maximize-happiness-of-selected-children/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_happiness_sum(self, happiness: list[int], k: int) -> int:
        """
        maximum happniess sum
        """
        h_sorted = sorted(happiness, reverse=True)
        t = 0
        h_sum = 0
        remain_turns = k

        while remain_turns and h_sorted[t] > t:
            h_sum += h_sorted[t] - t
            remain_turns -= 1
            t += 1

        return h_sum
