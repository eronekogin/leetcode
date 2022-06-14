"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
"""


from collections import defaultdict


class Solution:
    def minTime(
        self,
        n: int,
        edges: list[list[int]],
        hasApple: list[bool]
    ) -> int:
        def walk(currNode: int) -> int:
            if currNode in visited:
                return 0

            visited.add(currNode)
            steps = 0

            # Collecting apples in the sub tree.
            for nextNode in graph[currNode]:
                steps += walk(nextNode)

            # Then back to its parent node.
            if steps > 0:
                return steps + 2

            # No apple in the subtree, but having apple at the current node.
            if hasApple[currNode]:
                return 2

            # No apple at the current node.
            return 0

        visited = set()

        # Build graph.
        graph = defaultdict(list)
        for src, dest in edges:
            graph[src].append(dest)
            graph[dest].append(src)

        # As the node zero does not have a parent, so we need to subtract 2
        # from it to get the final total steps.
        return max(walk(0) - 2, 0)
