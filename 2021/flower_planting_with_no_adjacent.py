"""
https://leetcode.com/problems/flower-planting-with-no-adjacent/
"""


class Solution:
    def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
        ALL_COLORS = {1, 2, 3, 4}
        answers = [0] * n

        # Build graph based on paths.
        graph = [[] for _ in range(n)]
        for src, dst in paths:
            graph[src - 1].append(dst - 1)
            graph[dst - 1].append(src - 1)

        # Color node with any available color until reaching the end.
        # since each node could only contain at most 3 paths, it will always
        # have an available color to fill.
        for src in range(n):
            currColors = {answers[dst] for dst in graph[src]}
            availableColors = ALL_COLORS - currColors
            answers[src] = availableColors.pop()

        return answers
