"""
https://leetcode.com/problems/words-within-two-edits-of-dictionary/description/
"""


class Solution:
    """
    Solution
    """

    def two_edit_words(self, queries: list[str], dictionary: list[str]) -> list[str]:
        """
        two edit words
        """
        def check(q: str):
            for w in words:
                if sum(x != y for x, y in zip(q, w)) <= 2:
                    return True

            return False

        words = list(set(dictionary))
        return [
            q
            for q in queries
            if check(q)
        ]
