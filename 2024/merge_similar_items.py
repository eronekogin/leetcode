"""
https://leetcode.com/problems/merge-similar-items/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def merge_similar_items(
        self,
        items1: list[list[int]],
        items2: list[list[int]]
    ) -> list[list[int]]:
        """
        merge similar items
        """
        cnt = Counter()
        for v, w in items1:
            cnt[v] += w

        for v, w in items2:
            cnt[v] += w

        return [[v, cnt[v]] for v in sorted(cnt.keys())]
