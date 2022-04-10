"""
https://leetcode.com/problems/clone-graph/
"""


from test_helper import GraphNode
from collections import deque


class Solution:
    def cloneGraph(self, node: GraphNode) -> GraphNode:
        """
        Use BFS solution.
        """
        if not node:  # Empty graph.
            return node

        visited = {node: GraphNode(node.val, [])}
        queue = deque([node])
        while queue:
            currNode = queue.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = GraphNode(neighbor.val, [])
                    queue.append(neighbor)

                visited[currNode].neighbors.append(visited[neighbor])

        return visited[node]
