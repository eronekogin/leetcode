"""
https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/description/
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

        start = 0
        match = len(c2)
        rslt = 0

        for w in word1:
            c2[w] -= 1
            match -= c2[w] == 0

            while match == 0:
                match += c2[word1[start]] == 0
                c2[word1[start]] += 1
                start += 1

            rslt += start

        return rslt
