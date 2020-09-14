"""
https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
"""

from test_helper import QuadTreeNode


class Solution:
    def intersect(
            self,
            quadTree1: QuadTreeNode,
            quadTree2: QuadTreeNode) -> QuadTreeNode:
        if quadTree1.isLeaf:
            if quadTree1.val:
                return quadTree1
            else:
                return quadTree2
        elif quadTree2.isLeaf:
            if quadTree2.val:
                return quadTree2
            else:
                return quadTree1
        else:
            tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and (
                    tl.val == tr.val == bl.val == br.val):
                return QuadTreeNode(tl.val, True, None, None, None, None)

            return QuadTreeNode(False, False, tl, tr, bl, br)
