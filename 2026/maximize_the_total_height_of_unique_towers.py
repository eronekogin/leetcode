"""
https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_total_sum(self, maximum_height: list[int]) -> int:
        """
        maximum total sum
        """
        total = 0
        maximum_height.sort(reverse=True)
        curr_max = maximum_height[0] + 1

        for h in maximum_height:
            if h < curr_max:
                total += h
                curr_max = h
            else:
                if curr_max > 1:
                    curr_max -= 1
                    total += curr_max
                else:
                    return -1

        return total
