"""
https://leetcode.com/problems/trim-a-binary-search-tree/
"""


from test_helper import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        def cut(currRoot: TreeNode) -> TreeNode:
            if not currRoot:
                return None

            if currRoot.val > high:
                return cut(currRoot.left)

            if currRoot.val < low:
                return cut(currRoot.right)

            currRoot.left = cut(currRoot.left)
            currRoot.right = cut(currRoot.right)
            return currRoot

        return cut(root)


root = TreeNode(1)
root.create_tree({
    1: (0, 2)
})
print(Solution().trimBST(root, 1, 2))
