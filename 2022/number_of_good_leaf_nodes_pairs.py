"""
https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
"""

from test_helper import TreeNode


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def walk(node: TreeNode) -> list[int]:
            nonlocal cnt

            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left = walk(node.left)
            right = walk(node.right)

            cnt += sum(l + r <= distance for l in left for r in right)

            return [n + 1 for n in left + right if n + 1 < distance]

        cnt = 0
        walk(root)
        return cnt
