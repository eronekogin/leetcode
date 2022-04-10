"""
https://leetcode.com/problems/validate-binary-tree-nodes/
"""


class Solution:
    def validateBinaryTreeNodes(
        self,
        n: int,
        leftChild: list[int],
        rightChild: list[int]
    ) -> bool:
        visitedNodes = set()

        # Find root first.
        rootSet = (
            {i for i in range(n)} -
            (set(leftChild) | set(rightChild))
        )

        if len(rootSet) != 1:
            return False  # No root found.

        currNodes = [rootSet.pop()]
        for node in currNodes:
            if node in visitedNodes:
                return False

            visitedNodes.add(node)
            if leftChild[node] > -1:
                currNodes.append(leftChild[node])

            if rightChild[node] > -1:
                currNodes.append(rightChild[node])

        return len(visitedNodes) == n


print(Solution().validateBinaryTreeNodes(4, [3, -1, 1, -1], [-1, -1, 0, -1]))
