"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
"""


from test_helper import TreeNode


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        currNode = root
        stack = []
        currSum = 0
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.right

            currNode = stack.pop()
            currSum += currNode.val
            currNode.val = currSum
            currNode = currNode.left

        return root


root = TreeNode(4)
root.create_tree({
    4: (1, 6),
    1: (0, 2),
    2: (None, 3),
    6: (5, 7),
    7: (None, 8)
})
print(Solution().bstToGst(root).print_tree())
