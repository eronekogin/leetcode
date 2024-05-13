"""
https://leetcode.com/problems/root-equals-sum-of-children/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def check_tree(self, root: TreeNode) -> bool:
        """
        check tree
        """
        return root.val == root.left.val + root.right.val
