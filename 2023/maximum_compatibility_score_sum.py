"""
https://leetcode.com/problems/maximum-compatibility-score-sum/
"""


from functools import cache


class Solution:
    def maxCompatibilitySum(self, students: list[list[int]], mentors: list[list[int]]) -> int:
        @cache
        def dp(mask: int, c: int):
            maxScore = 0
            for r in range(M):
                if not mask & (1 << r):  # Student r is not assigned.
                    maxScore = max(maxScore, dp(mask ^ (1 << r), c - 1) + scores[r][c])
            
            return maxScore


        # Calculate score matrix first.
        M = len(students)
        scores = [[0] * M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                scores[r][c] = sum(x == y for x, y in zip(students[r], mentors[c]))
        
        return dp(1 << M, M - 1)
