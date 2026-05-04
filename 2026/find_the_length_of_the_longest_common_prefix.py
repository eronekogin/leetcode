"""
https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/description/
"""


class Solution:
    """
    Solution
    """

    def longest_common_prefix(self, arr1: list[int], arr2: list[int]) -> int:
        """
        longest common prefix
        """
        trie = {}
        for x in arr1:
            curr = trie
            for c in str(x):
                if c not in curr:
                    curr[c] = {}

                curr = curr[c]

        max_len = 0
        for y in arr2:
            curr = trie
            curr_len = 0
            for c in str(y):
                if c not in curr:
                    break

                curr = curr[c]
                curr_len += 1

            max_len = max(max_len, curr_len)

        return max_len
