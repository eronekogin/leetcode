"""
https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def valid_substring_count(self, word1: str, word2: str) -> int:
        """
        valid substring count
        """
        c2 = Counter(word2)

        match, res, j = len(c2), 0, 0
        for ch in word1:
            c2[ch] -= 1
            match -= c2[ch] == 0

            while match == 0:  # Found a valid string
                match += c2[word1[j]] == 0
                c2[word1[j]] += 1
                j += 1

            # the previous chars until j index can be used
            # to form valid strings with the current widow
            res += j

        return res
