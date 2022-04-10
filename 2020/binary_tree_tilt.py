"""
https://leetcode.com/problems/binary-tree-tilt/
"""


from test_helper import TreeNode


class Solution:
    def __init__(self):
        self._tilt = 0

    def findTilt(self, root: TreeNode) -> int:
        def get_sum(root: TreeNode) -> int:
            if not root:
                return 0

            left, right = get_sum(root.left), get_sum(root.right)
            self._tilt += abs(left - right)
            return left + root.val + right

        get_sum(root)
        return self._tilt
