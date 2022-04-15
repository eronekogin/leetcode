"""
https://leetcode.com/problems/linked-list-in-binary-tree/
"""


from test_helper import ListNode, TreeNode


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def dfs(head: ListNode, root: TreeNode) -> bool:
            if not head:
                return True

            if not root:
                return False

            return (
                head.val == root.val and
                (
                    dfs(head.next, root.left) or
                    dfs(head.next, root.right)
                )
            )

        if not head:
            return True

        if not root:
            return False

        return (
            dfs(head, root) or
            self.isSubPath(head, root.left) or
            self.isSubPath(head, root.right)
        )


root = TreeNode(1)
root.left = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.left = TreeNode(1)
root.right.left.right.right = TreeNode(3)

head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(8)

print(Solution().isSubPath(head, root))
