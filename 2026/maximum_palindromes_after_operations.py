"""
https://leetcode.com/problems/maximum-palindromes-after-operations/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def max_palindromes_after_operations(self, words: list[str]) -> int:
        """
        max palindromes after operations
        """
        cnt = Counter(c for w in words for c in w)
        pairs = sum(v >> 1 for v in cnt.values())

        for i, x in enumerate(sorted(map(len, words))):
            pairs -= x >> 1
            if pairs < 0:
                return i

        return len(words)
