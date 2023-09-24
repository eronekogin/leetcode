"""
https://leetcode.com/problems/find-if-path-exists-in-graph/
"""


from collections import deque, defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        # Build graph.
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # bfs walkthrough.
        queue = deque([source])
        visited = {source}
        while queue:
            currNode = queue.popleft()
            if currNode == destination:
                return True
            
            for node in graph[currNode]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        
        return False
        