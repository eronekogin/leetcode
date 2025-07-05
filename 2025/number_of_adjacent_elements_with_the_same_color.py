"""
https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description/
"""


class Solution:
    """
    Solution
    """

    def color_the_array(self, n: int, queries: list[list[int]]) -> list[int]:
        """
        color the array
        """
        colors = [0] * n
        pairs = 0
        rslt: list[int] = []

        for i, c in queries:
            prev_color = colors[i - 1] if i > 0 else 0
            next_color = colors[i + 1] if i + 1 < n else 0
            origin_color = colors[i]
            colors[i] = c
            pairs += (
                (prev_color == c) +
                (next_color == c) -
                (prev_color == origin_color > 0) -
                (next_color == origin_color > 0)
            )
            rslt.append(pairs)

        return rslt


print(Solution().color_the_array(4, [[0, 2], [1, 2], [3, 1], [1, 1], [2, 1]]))
