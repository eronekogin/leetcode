"""
https://leetcode.com/problems/count-pairs-that-form-a-complete-day-ii/description/
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
        cnt = 0

        for i in range(13):
            p = (24 - i) % 24
            if i not in remainders or p not in remainders:
                continue

            if i == p:
                cnt += remainders[i] * (remainders[i] - 1) // 2
            else:
                cnt += remainders[i] * remainders[p]

        return cnt
