"""
https://leetcode.com/problems/cousins-in-binary-tree/
"""


from test_helper import TreeNode


from collections import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False

        px = py = dx = dy = None

        # (parent node value, depth, currNode)
        queue = deque([(None, 0, root)])
        while queue:
            parent, depth, currNode = queue.popleft()
            if currNode:
                v = currNode.val
                if v == x:
                    px, dx = parent, depth

                if v == y:
                    py, dy = parent, depth

                if px and py:  # x and y are both found now.
                    if px != py and dx == dy:
                        return True
                    else:
                        return False

                queue.append((v, depth + 1, currNode.left))
                queue.append((v, depth + 1, currNode.right))

        return False  # x or y or both are not found.
