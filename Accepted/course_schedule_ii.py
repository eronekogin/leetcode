"""
https://leetcode.com/problems/course-schedule-ii/
"""


from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(
            self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Use BFS to perform topological sort.
        """
        todo, nodesWithPre = defaultdict(list), {}
        for curr, pre in prerequisites:  # Build from input.
            todo[pre].append(curr)
            nodesWithPre[curr] = nodesWithPre.get(curr, 0) + 1

        # Put all nodes which have empty pre nodes into the queue.
        queue = deque([i for i in range(numCourses) if i not in nodesWithPre])
        rslt = []
        while queue:
            pre = queue.popleft()
            rslt.append(pre)
            for curr in todo[pre]:
                nodesWithPre[curr] -= 1
                if not nodesWithPre[curr]:  # The current node has no pre.
                    queue.append(curr)

        if len(rslt) != numCourses:
            return []

        return rslt
