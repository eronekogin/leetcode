"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""


from test_helper import TreeNode


class Solution:
    def lowestCommonAncestor(
            self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack, parents, ancestors = [root], {root: None}, set()

        # While searching p and q, store their parents to parents dictionary.
        while p not in parents or q not in parents:
            currNode = stack.pop()
            left, right = currNode.left, currNode.right
            if left:
                parents[left] = currNode
                stack.append(left)

            if right:
                parents[right] = currNode
                stack.append(right)

        currNode = p
        while currNode:  # Generate parent path for node p.
            ancestors.add(currNode)
            currNode = parents[currNode]

        currNode = q
        while currNode not in ancestors:  # Scan for q's parents.
            currNode = parents[currNode]

        return currNode
