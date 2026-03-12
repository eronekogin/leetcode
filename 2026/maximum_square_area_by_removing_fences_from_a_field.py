"""
https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/description/
"""


class Solution:
    """
    Solution
    """

    def maximize_square_area(self, m: int, n: int, h: list[int], v: list[int]) -> int:
        """
        maximize square area
        """
        def get_candidates(fences: list[int], border: int) -> set[int]:
            points = sorted([1] + fences + [border])
            return {
                points[j] - points[i]
                for i in range(len(points))
                for j in range(i + 1, len(points))
            }

        h_candidates = get_candidates(h, m)
        v_candidates = get_candidates(v, n)

        max_side = max(
            h_candidates & v_candidates,
            default=0
        )

        if max_side > 0:
            return (max_side * max_side) % (10 ** 9 + 7)

        return -1
