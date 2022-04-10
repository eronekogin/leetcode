"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""


from collections import deque

from test_helper import TreeNode


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        while True:
            currNode = queue.popleft()
            if not currNode.left:
                if currNode.right:
                    return False
                else:  # Found the first leaf node.
                    break

            queue.append(currNode.left)
            if not currNode.right:  # Found the parent of the first leaf node.
                break

            queue.append(currNode.right)

        # From this moment, we have two cases:
        # 1. When it jumps from the first leaf node, all the following node
        #   in the remaining queue should not have any child node.
        # 2. When it jumps from the parent of the first leaf node, then it
        #   also means all the following node the remaining queue should
        #   not have any child node.
        return not any(node.left or node.right for node in queue)


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (None, None),
    3: (7, 8)
})
print(Solution().isCompleteTree(root))
