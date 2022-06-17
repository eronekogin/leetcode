"""
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def walk(currNode: TreeNode, maxVal: int) -> None:
            if not currNode:
                return

            if currNode.val >= maxVal:
                self.rslt += 1
                maxVal = currNode.val

            walk(currNode.left, maxVal)
            walk(currNode.right, maxVal)

        self.rslt = 0
        walk(root, float('-inf'))
        return self.rslt
