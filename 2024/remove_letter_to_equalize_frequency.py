"""
https://leetcode.com/problems/remove-letter-to-equalize-frequency/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def equal_frequency(self, word: str) -> bool:
        """
        equal frequency
        """
        cnt = Counter(word)
        for w in word:
            cnt[w] -= 1

            if cnt[w] == 0:
                del cnt[w]

            if len(set(cnt.values())) == 1:
                return True

            cnt[w] += 1

        return False
