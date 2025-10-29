"""
https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/description/
"""


class Solution:
    """
    Solution
    """

    def get_max_function_value(self, receiver: list[int], k: int) -> int:
        """
        positions[end][start] stands for the final position when starting jump
        from start with 2**end steps, so we have:
            middle = positions[end - 1][start]
            positions[end][start] = positions[end - 1][middle]

        profits[end][start] stands for the sum of indices when tarting jump
        from start with 2**end steps, so we have:
            profits[end][start] = (
                profits[end - 1][start] +
                profits[end - 1][middle]
            )
        """
        limit = 35
        n = len(receiver)
        positions = [receiver[:] for _ in range(limit)]
        profits = [list(range(n)) for _ in range(limit)]

        for end in range(1, limit):
            for start in range(n):
                middle = positions[end - 1][start]
                positions[end][start] = positions[end - 1][middle]
                profits[end][start] = (
                    profits[end - 1][start] +
                    profits[end - 1][middle]
                )

        max_score = 0
        for start in range(n):
            score = 0
            for end in range(limit):
                if ((k + 1) >> end) & 1:
                    score += profits[end][start]
                    start = positions[end][start]

            max_score = max(max_score, score)

        return max_score
