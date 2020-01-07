"""
https://leetcode.com/problems/course-schedule/
"""


from typing import List
from collections import deque


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Use topology sort algorithm, the visualization is as follows:

        N = 6  # Has no cycle.
        p = [[2,1],[4,1],[3,2],[5,4]]

        0
             1
           /   \
          2     4 
         /       \
        3         5

        # Initial:
        todo = {0: set(), 1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
        graph =  {1: {2, 4}, 2: {3}, 4: {5}})

        # Processing:
        node 0
        todo = {1: set(), 2: {1}, 3: {2}, 4: {1}, 5: {4}}
        node 1
        todo = {2: set(), 3: {2}, 4: set(), 5: {4}}
        node 2
        todo = {3: set(), 4: set(), 5: {4}}
        node 4
        todo = {3: set(), 5: set()}
        node 3
        todo = {5: set()}
        node 5
        todo= {}

        N = 6  # Has cycle.
        p = [[2,1],[4,1],[3,2],[5,4],[2,3]]

        0
             1
           /   \
          2     4 
         //       \
        3          5

        # Initial: 
        todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
        graph =  {1: {2, 4}, 2: {3}, 4: {5}, 3: {2}})

        # Processing:
        todo = {0: set(), 1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
        node 0
        todo = {1: set(), 2: {1, 3}, 3: {2}, 4: {1}, 5: {4}}
        node 1
        todo = {2: {3}, 3: {2}, 4: set(), 5: {4}}
        node 4
        todo ={2: {3}, 3: {2}, 5: set()}
        node 5
        todo ={2: {3}, 3: {2}}
        """
        todo = {i: set() for i in range(numCourses)}
        graph = {i: set() for i in range(numCourses)}
        for curr, pre in prerequisites:
            todo[curr].add(pre)
            graph[pre].add(curr)

        queue = deque([k for k in todo if not todo[k]])
        while queue:
            pre = queue.popleft()
            for curr in graph[pre]:
                todo[curr].remove(pre)
                if not todo[curr]:
                    queue.append(curr)

            todo.pop(pre)

        return not todo
