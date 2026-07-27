"""
https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
"""


class Solution:
    """
    Solution
    """

    def query_results(self, limit: int, queries: list[list[int]]) -> list[int]:
        """
        query results
        """
        colors_to_balls: dict[int, int] = {}
        balls_to_colors: dict[int, int] = {}
        rslt: list[int] = []

        for i, curr_color in queries:
            if i in balls_to_colors:
                prev_color = balls_to_colors[i]
                if prev_color in colors_to_balls:
                    colors_to_balls[prev_color] -= 1
                    if not colors_to_balls[prev_color]:
                        del colors_to_balls[prev_color]

            balls_to_colors[i] = curr_color
            if curr_color not in colors_to_balls:
                colors_to_balls[curr_color] = 0

            colors_to_balls[curr_color] += 1
            rslt.append(len(colors_to_balls))

        return rslt


print(Solution().query_results(1, [[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]))
