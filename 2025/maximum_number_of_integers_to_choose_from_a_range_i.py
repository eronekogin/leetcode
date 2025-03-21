"""
https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/description/
"""


class Solution:
    """
    Solution
    """

    def max_count(self, banned: list[int], n: int, max_sum: int) -> int:
        """
        max count
        """
        curr_sum = 0
        cnt = 0
        banned_set = set(banned)
        for i in range(1, n + 1):
            if i not in banned_set:
                cnt += 1
                curr_sum += i

            if curr_sum >= max_sum:
                break

        return cnt - (curr_sum > max_sum)
