"""
https://leetcode.com/problems/solving-questions-with-brainpower/description/
"""


class Solution:
    """
    Solution
    """

    def most_points(self, questions: list[list[int]]) -> int:
        """
        most points
        """
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            point, power = questions[i]
            dp[i] = max(
                point + dp[min(n, i + power + 1)],
                dp[i + 1]
            )

        return dp[0]


print(Solution().most_points([[3, 2], [4, 3], [4, 4], [2, 5]]))
