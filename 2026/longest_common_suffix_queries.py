"""
https://leetcode.com/problems/longest-common-suffix-queries/description/
"""


class Solution:
    """
    Solution
    """

    def string_indices(self, words_container: list[str], words_query: list[str]) -> list[int]:
        """
        string indices
        """
        sorted_words = list(enumerate(words_container))
        sorted_words.sort(key=lambda x: (len(x[1]), x[0]))
        empty_suffix_index = sorted_words[0][0]

        trie = {}
        for i, w in sorted_words:
            curr = trie
            for c in reversed(w):
                if c not in curr:
                    curr[c] = {}

                curr = curr[c]

                if '#' not in curr:
                    curr['#'] = i

        rslt: list[int] = []
        for q in words_query:
            curr = trie
            for c in reversed(q):
                if c not in curr:
                    break

                curr = curr[c]

            rslt.append(curr.get('#', empty_suffix_index))

        return rslt


print(Solution().string_indices(
    ["abcdefgh", "poiuygh", "ghghgh"], ["gh", "acbfgh", "acbfegh"]))
