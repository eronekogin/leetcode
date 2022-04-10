"""
https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
"""


from test_helper import TreeNode


from typing import List


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        """
        Taking advantage of BST and inorder traversal.
        """
        n1, n2, s1, s2, rslt = root1, root2, [], [], []
        while n1 or n2 or s1 or s2:
            while n1:
                s1.append(n1)
                n1 = n1.left

            while n2:
                s2.append(n2)
                n2 = n2.left

            if not s2 or (s1 and s1[-1].val <= s2[-1].val):
                n1 = s1.pop()
                rslt.append(n1.val)
                n1 = n1.right
            else:
                n2 = s2.pop()
                rslt.append(n2.val)
                n2 = n2.right

        return rslt


root1 = TreeNode(0)
root1.create_tree({
    0: (None, 59),
    59: (57, 90)
})
root2 = TreeNode(60)
root2.create_tree({
    60: (17, 74),
    17: (6, 20),
    74: (63, 97),
    97: (95, None)
})
print(list(Solution()._in_order(root1)))
