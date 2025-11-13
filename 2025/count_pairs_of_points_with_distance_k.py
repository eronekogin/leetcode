"""
https://leetcode.com/problems/count-pairs-of-points-with-distance-k/description/
"""


class Solution:
    """
    Solution
    """

    def count_pairs(self, coordinates: list[list[int]], k: int) -> int:
        """
        count pairs
        """
        cnt: dict[tuple[int, int], int] = {}
        pairs = 0
        for x, y in coordinates:
            for m in range(k + 1):
                target = (x ^ m, y ^ (k - m))
                pairs += cnt.get(target, 0)

            cnt[(x, y)] = cnt.get((x, y), 0) + 1

        return pairs
