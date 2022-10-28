"""
https://leetcode.com/problems/best-team-with-no-conflicts/
"""


class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        """
        The maximum age is <= 1000 given by the question constraints, so it is
        fairy faster to search in a subset of max age length list.
        """
        maxAge = max(ages)
        maxScores = [0] * (maxAge + 1)
        for score, age in sorted(zip(scores, ages)):
            maxScores[age] = score + max(maxScores[:age + 1])

        return max(maxScores)
