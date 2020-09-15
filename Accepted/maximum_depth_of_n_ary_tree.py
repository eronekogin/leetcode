"""
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""


from test_helper import NaryTreeNode


class Solution:
    def maxDepth(self, root: NaryTreeNode) -> int:
        if not root:
            return 0

        currNodes, depth = [root], 0
        while currNodes:
            depth += 1
            nextNodes = []
            for node in currNodes:
                if node.children:
                    nextNodes += node.children

            currNodes = nextNodes

        return depth
