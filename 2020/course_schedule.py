"""
https://leetcode.com/problems/course-schedule/
"""


from typing import List
from collections import deque, defaultdict


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Use BFS to perform topological sort.
        """
        todo, nodesWithPre = defaultdict(list), {}
        for curr, pre in prerequisites:  # Build from input.
            todo[pre].append(curr)
            nodesWithPre[curr] = nodesWithPre.get(curr, 0) + 1

        # Put all nodes which have empty pre nodes into the queue.
        queue = deque([i for i in range(numCourses) if i not in nodesWithPre])
        while queue:
            pre = queue.popleft()
            for curr in todo[pre]:
                nodesWithPre[curr] -= 1
                if not nodesWithPre[curr]:  # The current node has no pre.
                    queue.append(curr)

            todo.pop(pre)

        return not todo
