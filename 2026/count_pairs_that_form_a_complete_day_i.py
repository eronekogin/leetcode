"""
https://leetcode.com/problems/count-pairs-that-form-a-complete-day-i/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_complete_day_pairs(self, hours: list[int]) -> int:
        """
        count complete day pairs
        """
        remainders = Counter(h % 24 for h in hours)
        cnt = remainders[0] * (remainders[0] - 1) // 2
        for r in range(1, 13):
            if r not in remainders:
                continue

            v = remainders[r]
            c = 24 - r
            if c == r:
                cnt += v * (v - 1) // 2
            else:
                cnt += v * remainders[c]

        return cnt


print(Solution().count_complete_day_pairs([20, 48, 24]))
