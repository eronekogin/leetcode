"""
https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/
"""


from test_helper import TreeNode


class Solution:
    """
    Solution
    """

    def average_of_subtree(self, root: TreeNode) -> int:
        """
        average of subtree
        """
        def dfs(root: TreeNode | None) -> tuple[int, int]:
            nonlocal cnt

            if not root:
                return (0, 0)

            left_nodes, left_sum = dfs(root.left)
            right_nodes, right_sum = dfs(root.right)
            curr_nodes = left_nodes + right_nodes + 1
            curr_sum = left_sum + right_sum + root.val

            cnt += (curr_sum // curr_nodes == root.val)

            return (curr_nodes, curr_sum)

        cnt = 0
        dfs(root)
        return cnt
