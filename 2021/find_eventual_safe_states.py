"""
https://leetcode.com/problems/find-eventual-safe-states/
"""


from collections import deque


class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        """
        1. For those nodes having no outgoing edges, they are already safe
            nodes.
        2. Then for the node which has outgoing edges only to those safe nodes,
            then this node will also be safe.
        3. Continue doing this until all nodes in the graph has been scanned.
        """
        N = len(graph)
        outgoings = [set(nodes) for nodes in graph]
        incomings = [set() for _ in range(N)]
        safes = [False] * N

        # Collect incomings and also set initial safe nodes to a queue.
        queue = deque([])
        for node, outgoingNodes in enumerate(outgoings):
            if not outgoingNodes:
                queue.append(node)

            for outGoingNode in outgoingNodes:
                incomings[outGoingNode].add(node)

        # Collect other safe nodes.
        while queue:
            safeNode = queue.popleft()
            safes[safeNode] = True
            for incomingNode in incomings[safeNode]:
                outgoings[incomingNode].remove(safeNode)
                if not outgoings[incomingNode]:
                    queue.append(incomingNode)

        return [node for node, isSafe in enumerate(safes) if isSafe]
