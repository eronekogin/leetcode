"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
"""


from test_helper import TreeNode
from collections import deque


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        """
        Numbering each node with a unique index starting from the root node.
        The index keeps increasing even for null node. Then the width of each
        level is the end node's index - the start node's index + 1.
        """
        if not root:
            return 0

        queue = deque([(0, 1, root)])  # (level, index, node)
        preLevel, maxWidth = 0, 1
        currStart = currEnd = 1
        while queue:
            currLevel, currIdx, currNode = queue.popleft()
            if preLevel != currLevel:  # A new level start.
                preLevel = currLevel
                maxWidth = max(maxWidth, currEnd - currStart + 1)
                currStart = currIdx

            currEnd = currIdx
            nextLevel, nextIdx = currLevel + 1, currIdx << 1
            if currNode.left:
                queue.append((nextLevel, nextIdx, currNode.left))

            if currNode.right:
                queue.append((nextLevel, nextIdx + 1, currNode.right))

        # Calculate the last level.
        maxWidth = max(maxWidth, currEnd - currStart + 1)

        return maxWidth

    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        """
        Same idea with much shorter form.
        """
        if not root:
            return 0

        nodesOnEachLevel = [(1, root)]  # (index, node)
        maxWidth = 1
        while nodesOnEachLevel:
            maxWidth = max(
                maxWidth, nodesOnEachLevel[-1][0] - nodesOnEachLevel[0][0] + 1)

            nodesOnEachLevel = [
                nextItem
                for preIdx, preNode in nodesOnEachLevel
                for nextItem in enumerate(
                    (preNode.left, preNode.right), start=preIdx << 1)
                if nextItem[1]
            ]

        return maxWidth


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (4, 5),
    3: (None, 7)
})
print(Solution().widthOfBinaryTree(root))
