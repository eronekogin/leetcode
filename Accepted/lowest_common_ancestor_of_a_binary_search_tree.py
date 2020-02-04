"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def lowestCommonAncestor(
            self,
            root: TreeNode,
            p: TreeNode,
            q: TreeNode) -> TreeNode:
        currRoot, vp, vq = root, p.val, q.val
        while True:
            vr = currRoot.val
            if vr < vp and vr < vq:
                currRoot = currRoot.right
            elif vr > vp and vr > vq:
                currRoot = currRoot.left
            else:
                return currRoot
