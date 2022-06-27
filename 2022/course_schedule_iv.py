"""
https://leetcode.com/problems/course-schedule-iv/
"""


from collections import defaultdict
from functools import lru_cache


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]]
    ) -> list[bool]:
        @lru_cache(None)
        def dfs(src: int, target: int) -> bool:
            if src == target:
                return True

            return any(
                dfs(node, target)
                for node in graph[src]
            )

        graph = defaultdict(list)
        for src, dst in prerequisites:
            graph[src].append(dst)

        return [
            dfs(src, target)
            for src, target in queries
        ]
