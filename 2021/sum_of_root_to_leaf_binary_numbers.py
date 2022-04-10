"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


from test_helper import TreeNode


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        currNodes = [(0, root)]
        while currNodes:
            nextNodes = []
            for preSum, node in currNodes:
                currSum = (preSum << 1) + node.val
                if not node.left and not node.right:  # Found a leaf node.
                    total += currSum
                else:
                    if node.left:
                        nextNodes.append((currSum, node.left))

                    if node.right:
                        nextNodes.append((currSum, node.right))

            currNodes = nextNodes

        return total
