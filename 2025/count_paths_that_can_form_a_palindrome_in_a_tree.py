"""
https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/description/
"""


from collections import Counter
from functools import cache


class Solution:
    """
    Solution
    """

    def count_palindrome_paths(self, parent: list[int], s: str) -> int:
        """
        count palindrome paths
        """
        @cache
        def node_to_root_mask(node: int) -> int:
            if node == 0:
                return 0

            return node_to_root_mask(parent[node]) ^ (1 << (ord(s[node]) - base))

        base = ord('a')
        cnt = Counter()
        pairs = 0

        for node in range(len(parent)):
            # left ^ (left ^ (1 << j)) = (1 << j), which means
            # there is at most only 1 char set in the middle
            # which can form a palindrome
            left = node_to_root_mask(node)
            pairs += cnt[left] + sum(cnt[left ^ (1 << j)] for j in range(26))
            cnt[left] += 1

        return pairs
