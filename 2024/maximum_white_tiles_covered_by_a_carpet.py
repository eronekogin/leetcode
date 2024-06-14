"""
https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/description/
"""


from bisect import bisect_right


class Solution:
    """
    Solution
    """

    def maximum_white_tiles(self, tiles: list[list[int]], carpet_len: int) -> int:
        """
        maximum white tiles
        """
        sorted_tiles = sorted(tiles, key=lambda x: x[0])
        start_indexes = [s for s, _ in sorted_tiles]
        prefix_sums = [0]
        for s, e in sorted_tiles:
            prefix_sums.append(prefix_sums[-1] + e - s + 1)

        max_covered = 0

        for i, (s, e) in enumerate(sorted_tiles):
            max_end = s + carpet_len - 1
            if e >= max_end:  # One tile is large enough
                return carpet_len

            next_tile_start = bisect_right(start_indexes, max_end) - 1
            not_covered = 0

            if sorted_tiles[next_tile_start][1] > max_end:
                not_covered = sorted_tiles[next_tile_start][1] - max_end

            max_covered = max(
                max_covered,
                prefix_sums[next_tile_start + 1] - prefix_sums[i] - not_covered
            )

        return max_covered
