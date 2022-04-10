"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def distanceK(
            self, root: TreeNode, target: TreeNode, K: int) -> list[int]:
        def set_parents(root: TreeNode, parent: TreeNode) -> None:
            if root:
                root.parent = parent
                set_parents(root.left, root)
                set_parents(root.right, root)

        set_parents(root, None)
        currNodes = [target]
        visited = {target}
        for _ in range(K):
            nextNodes = []
            for currNode in currNodes:
                for node in [currNode.left, currNode.right, currNode.parent]:
                    if node and node not in visited:
                        visited.add(node)
                        nextNodes.append(node)

            currNodes = nextNodes

        return [node.val for node in currNodes]
