"""
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


from test_helper import TreeNode


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        currNode, stack, pre = root, [], 0
        while currNode or stack:
            while currNode:
                stack.append(currNode)
                currNode = currNode.right

            currNode = stack.pop()
            currNode.val += pre
            pre = currNode.val
            currNode = currNode.left

        return root


root = TreeNode(5)
root.create_tree({
    5: (2, 13)
})
print(Solution().convertBST(root))
