"""
https://leetcode.com/problems/image-overlap/
"""


from collections import Counter


class Solution:
    def largestOverlap(
            self, img1: list[list[int]], img2: list[list[int]]) -> int:
        """
        1. Collect all the cells in both img1 and img2 where the value of the
            cell is 1.
        2. Then comparing any such cells in both img1 and img2 and count its
            shifted positions by (r1 - r2, c1 - c2).
        3. Cells with same shift positions will form the final overlapped cells.
        4. Then get the maximum count or zero if there is no 1 in img1 or img2.
        """
        def get_ones(img: list[list[int]]) -> list[tuple[int]]:
            return [
                (r, c)
                for r, row in enumerate(img)
                for c, v in enumerate(row)
                if v]

        l1, l2 = get_ones(img1), get_ones(img2)
        cnt = Counter((r1 - r2, c1 - c2) for r1, c1 in l1 for r2, c2 in l2)
        return max(cnt.values() or [0])
