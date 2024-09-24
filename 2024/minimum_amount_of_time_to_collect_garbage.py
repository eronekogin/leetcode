"""
https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/description/
"""


class Solution:
    """
    Solution
    """

    def garbage_collection(self, garbage: list[str], travel: list[int]) -> int:
        """
        garbage collection
        """
        last_indexes = {'M': 0, 'P': 0, 'G': 0}
        cnt = 0
        for i, s in enumerate(garbage):
            for c in 'MPG':
                if c in s:
                    last_indexes[c] = i

            cnt += len(s)

        return (
            sum(sum(travel[:i]) for i in last_indexes.values() if i > 0) +
            cnt
        )
