"""
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""


from test_helper import TreeNode
from collections import deque


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        Use pre-order traverse to serialize the bst.
        """
        rslt, stack, currNode = [], [], root
        while stack or currNode:
            if currNode:
                rslt.append(str(currNode.val))
                stack.append(currNode)
                currNode = currNode.left
            else:
                currNode = stack.pop().right

        return ' '.join(rslt)

    def deserialize(self, data: str) -> TreeNode:
        """
        Use stack to rebuild the tree.
        """
        if not data:
            return None

        stack, vals = [], data.split()
        root = currNode = TreeNode(int(vals[0]))
        for i in range(1, len(vals)):
            val = int(vals[i])
            if val < currNode.val:
                currNode.left = TreeNode(val)
                stack.append(currNode)
                currNode = currNode.left
            else:
                while stack and stack[-1].val < val:
                    currNode = stack.pop()

                currNode.right = TreeNode(val)
                currNode = currNode.right

        return root


root = TreeNode(5)
root.create_tree({
    5: (3, 6),
    3: (2, 4),
    2: (1, None)
})
c = Codec()
s = c.serialize(root)
print(s)
print(c.deserialize(s).print_tree())
