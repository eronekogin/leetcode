"""
https://leetcode.com/problems/best-poker-hand/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def best_hand(self, ranks: list[int], suits: list[str]) -> str:
        """
        best hand
        """
        if len(set(suits)) == 1:
            return 'Flush'

        cnt = Counter(ranks)
        max_freq = max(cnt.values())

        if max_freq >= 3:
            return 'Three of a Kind'

        if max_freq >= 2:
            return 'Pair'

        return 'High Card'
