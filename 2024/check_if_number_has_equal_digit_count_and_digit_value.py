"""
https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def digit_count(self, num: str) -> bool:
        """
        digit count
        """
        cnt = Counter(num)
        return all(
            str(cnt[str(i)]) == c
            for i, c in enumerate(num)
        )
