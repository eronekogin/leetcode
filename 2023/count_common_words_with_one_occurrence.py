"""
https://leetcode.com/problems/count-common-words-with-one-occurrence/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def count_words(self, words1: list[str], words2: list[str]) -> int:
        """
        count_words
        """
        cnt1, cnt2 = Counter(words1), Counter(words2)
        return len(
            set(k for k, v in cnt1.items() if v == 1) &
            set(k for k, v in cnt2.items() if v == 1)
        )
