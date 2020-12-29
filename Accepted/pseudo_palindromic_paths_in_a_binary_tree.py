"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def search(currNode: TreeNode) -> None:
            if currNode:
                freqs[currNode.val - 1] += 1
                if not (currNode.left or currNode.right):
                    # Reach a leaf node.
                    if sum(f & 1 for f in freqs) <= 1:
                        self.paths += 1
                else:
                    search(currNode.left)
                    search(currNode.right)

                freqs[currNode.val - 1] -= 1  # Restore to search other paths.

        freqs = [0] * 9
        self.paths = 0
        search(root)
        return self.paths


r = TreeNode(2)
r.left = TreeNode(3)
r.right = TreeNode(1)
r.left.left = TreeNode(3)
r.left.right = TreeNode(1)
r.right.right = TreeNode(1)
print(Solution().pseudoPalindromicPaths(r))
