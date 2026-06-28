"""
https://leetcode.com/problems/make-a-square-with-the-same-color/description/
"""


class Solution:
    """
    Solution
    """

    def can_make_square(self, grid: list[list[str]]) -> bool:
        """
        can make square
        """
        def check(r: int, c: int):
            cnt = [0, 0]
            for i in [r, r + 1]:
                for j in [c, c + 1]:
                    if grid[i][j] == 'B':
                        cnt[0] += 1
                    else:
                        cnt[1] += 1

            return cnt[0] >= 3 or cnt[1] >= 3

        return any(
            [
                check(0, 0),
                check(0, 1),
                check(1, 0),
                check(1, 1)
            ]
        )
