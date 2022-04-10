"""
https://leetcode.com/problems/queens-that-can-attack-the-king/
"""


class Solution:
    def queensAttacktheKing(
        self,
        queens: list[list[int]],
        king: list[int]
    ) -> list[list[int]]:
        kr, kc = king
        left = right = up = down = None
        topLeft = topRight = bottomLeft = bottomRight = None
        for r, c in queens:
            if r == kr:  # Same row.
                if c < kc:  # Left.
                    if left is None or c > left[1]:
                        left = [r, c]
                else:  # Right.
                    if right is None or c < right[1]:
                        right = [r, c]
            elif c == kc:  # Same col.
                if r < kr:  # Up.
                    if up is None or r > up[0]:
                        up = [r, c]
                else:  # Down.
                    if down is None or r < down[0]:
                        down = [r, c]
            elif kc - c == r - kr:  # Same anti-diagonal.
                if c > kc:  # TopRight.
                    if topRight is None or c < topRight[1]:
                        topRight = [r, c]
                else:  # BottomLeft.
                    if bottomLeft is None or c > bottomLeft[1]:
                        bottomLeft = [r, c]
            elif kc - c == kr - r:  # Same diagonal.
                if c < kc:  # TopLeft.
                    if topLeft is None or c > topLeft[1]:
                        topLeft = [r, c]
                else:  # BottomRight.
                    if bottomRight is None or c < bottomRight[1]:
                        bottomRight = [r, c]

        return [x for x in [left, right, up, down, topLeft, topRight, bottomLeft, bottomRight] if x]
