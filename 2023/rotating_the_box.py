"""
https://leetcode.com/problems/rotating-the-box/
"""


class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        R, C = len(box), len(box[0])
        rslt = [[''] * R for _ in range(C)]

        for r in range(R - 1, -1, -1):
            row = box[r]
            bars = [c for c in range(C) if row[c] == '*']

            if not bars:  # No bars at all, all stones fall to the bottom.
                stones = sum(v == '#' for v in row)
                row = ['.'] * (C - stones) + ['#'] * stones
            else:
                bars = [-1] + bars + [C]
                for start, end in zip(bars, bars[1:]):
                    size = end - start - 1
                    stones = sum(row[i] == '#' for i in range(start + 1, end))
                    row[start + 1: end] = (
                        ['.'] * (size - stones) +
                        ['#'] * stones
                    )

            for c in range(C):
                rslt[c][R - 1 - r] = row[c]

        return rslt


print(Solution().rotateTheBox([["#", "#", "*", ".", "*", "."],
                               ["#", "#", "#", "*", ".", "."],
                               ["#", "#", "#", ".", "#", "."]]))
