"""
https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii/description/
"""


class Solution:
    """
    Solution
    """

    def count_prefix_suffix_pairs(self, words: list[str]) -> int:
        """
        Save the prefix + suffix pair of each word to a trie,
        and when we ever found a positive count on the current level,
        it means there was a word falls into this path and has the
        same prefix and suffix of the current word.
        """
        trie = {}
        cnt = 0

        for w in words:
            curr = trie
            for k in zip(w, reversed(w)):
                if k not in curr:
                    curr[k] = {}

                curr = curr[k]
                cnt += curr.get(0, 0)

            curr[0] = curr.get(0, 0) + 1

        return cnt
