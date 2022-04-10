"""
https://leetcode.com/problems/print-binary-tree/
"""


from test_helper import TreeNode


from typing import List


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def calc_height(root: TreeNode) -> int:
            if not root:
                return 0

            return 1 + max(calc_height(root.left), calc_height(root.right))

        def fill(currNode: TreeNode, r: int, start: int, end: int) -> None:
            if currNode:
                m = start + ((end - start) >> 1)
                rslt[r][m] = str(currNode.val)
                fill(currNode.left, r + 1, start, m - 1)
                fill(currNode.right, r + 1, m + 1, end)

        R = calc_height(root)
        C = (1 << R) - 1
        rslt = [[''] * C for _ in range(R)]
        fill(root, 0, 0, C - 1)
        return rslt


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (None, 4)
})
print(Solution().printTree(root))
