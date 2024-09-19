"""
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/
"""

from collections import defaultdict

from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def amount_of_time(self, root: TreeNode, start: int) -> int:
        """
        amount of time
        """
        children: defaultdict[int, list[int]] = defaultdict(list)
        parents: dict[int, int] = {root.val: root.val}
        curr_nodes: list[TreeNode] = [root]
        while curr_nodes:
            next_nodes: list[TreeNode] = []
            for node in curr_nodes:
                if node.left:
                    next_nodes.append(node.left)
                    parents[node.left.val] = node.val
                    children[node.val].append(node.left.val)

                if node.right:
                    next_nodes.append(node.right)
                    parents[node.right.val] = node.val
                    children[node.val].append(node.right.val)

            curr_nodes = next_nodes

        infected: set[int] = {start}
        curr_infected: list[int] = [start]
        minutes = 0
        while curr_infected:
            next_infected: list[int] = []
            for node in curr_infected:
                if parents[node] not in infected:
                    infected.add(parents[node])
                    next_infected.append(parents[node])

                for child in children[node]:
                    if child not in infected:
                        infected.add(child)
                        next_infected.append(child)

            curr_infected = next_infected
            minutes += 1

        return minutes - 1
