"""
https://leetcode.com/problems/even-odd-tree/
"""


from test_helper import TreeNode


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level = 0
        allNodesInCurrentLevel = [root]
        while allNodesInCurrentLevel:
            allNodesInNextLevel: list[TreeNode] = []
            preVal = None
            isOddLevel = level & 1
            for node in allNodesInCurrentLevel:
                if (
                    (node.val & 1 == isOddLevel) or
                    (
                        preVal is not None and
                        (
                            (isOddLevel and node.val >= preVal) or
                            (not isOddLevel and node.val <= preVal)
                        )
                    )
                ):
                    return False

                preVal = node.val
                if node.left:
                    allNodesInNextLevel.append(node.left)

                if node.right:
                    allNodesInNextLevel.append(node.right)

            level += 1
            allNodesInCurrentLevel = allNodesInNextLevel

        return True


root = TreeNode(1).create_tree(givenDict={
    1: (10, 4),
    10: (3, None),
    4: (7, 9),
    3: (12, 8),
    7: (6, None),
    9: (None, 2)
})

print(Solution().isEvenOddTree(root))
