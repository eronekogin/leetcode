"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""


from test_helper import TreeNode


class Solution:

    def serialize(self, root: TreeNode) -> str:
        """
        Serialize a binary tree in a level by level traverse.
        """
        rslt = []

        def do(currNode: TreeNode):
            if currNode:
                rslt.append(str(currNode.val))
                do(currNode.left)
                do(currNode.right)
            else:
                rslt.append('#')  # Placeholder for a null node.

        do(root)
        return ' '.join(rslt)

    def deserialize(self, data: str) -> TreeNode:
        """
        Deserialize the data with the same order.
        """
        vals = iter(data.split())

        def do() -> TreeNode:
            currVal = next(vals)
            if currVal == '#':
                return None

            root = TreeNode(int(currVal))
            root.left = do()
            root.right = do()

            return root

        return do()
