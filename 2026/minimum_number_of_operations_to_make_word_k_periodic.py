"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def minimum_operations_to_make_k_periodic(self, word: str, k: int) -> int:
        """
        minimum operations to make k periodic
        """
        cnt = Counter(
            word[i: i + k]
            for i in range(0, len(word), k)
        )

        f = max(cnt.values())

        return len(word) // k - f
