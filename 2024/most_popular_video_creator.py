"""
https://leetcode.com/problems/most-popular-video-creator/description/
"""


from collections import defaultdict


class Solution:
    """
    Solution
    """

    def most_popular_creator(
            self,
            creators: list[str],
            ids: list[str],
            views: list[int]
    ) -> list[list[str]]:
        """
        most popular creator
        """
        memo: defaultdict[str, dict[str, int]] = defaultdict(dict)
        popularity: defaultdict[str, int] = defaultdict(int)

        for c, i, v in zip(creators, ids, views):
            memo[c][i] = v
            popularity[c] += v

        max_popularity = max(popularity.values())

        rslt: list[list[str]] = []

        for c, p in popularity.items():
            if p == max_popularity:  # Found a candidate.
                max_view = -1
                max_id = ''
                for i, view in memo[c].items():
                    if view > max_view:
                        max_view = view
                        max_id = i
                    elif view == max_view and i < max_id:
                        max_id = i

                rslt.append([c, max_id])

        return rslt
