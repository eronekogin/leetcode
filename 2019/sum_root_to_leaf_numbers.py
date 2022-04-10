"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""


from collections import deque
from test_helper import TreeNode


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        Use level by level traverse.
        """
        if not root:  # Empty tree.
            return 0

        totalSum, queue = 0, deque([(root, root.val)])
        while queue:
            node, currSum = queue.popleft()
            if not node.left and not node.right:
                totalSum += currSum
                continue

            if node.left:
                queue.append((node.left, currSum * 10 + node.left.val))

            if node.right:
                queue.append((node.right, currSum * 10 + node.right.val))

        return totalSum


givenDict = {
    1: (2, 3)
}
root = TreeNode(1)
root.create_tree(givenDict)
print(Solution().sumNumbers(root))
