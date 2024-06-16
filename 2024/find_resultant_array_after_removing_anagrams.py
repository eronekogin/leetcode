"""
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def remove_anagrams(self, words: list[str]) -> list[str]:
        """
        remove anagrams
        """
        rslt: list[str] = []
        prev = Counter()
        for w in words:
            curr = Counter(w)
            if prev != curr:
                prev = curr
                rslt.append(w)

        return rslt
