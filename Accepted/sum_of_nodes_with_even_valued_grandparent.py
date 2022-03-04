"""
https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
"""


from test_helper import TreeNode


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        parents: dict[TreeNode, TreeNode] = {}
        currNodes: list[TreeNode] = [root]
        rslt = 0
        while currNodes:
            nextNodes: list[TreeNode] = []
            for currNode in currNodes:
                if (
                    currNode in parents and
                    parents[currNode] in parents and
                    parents[parents[currNode]].val & 1 == 0
                ):
                    rslt += currNode.val

                for nextNode in [currNode.left, currNode.right]:
                    if nextNode:
                        parents[nextNode] = currNode
                        nextNodes.append(nextNode)

            currNodes = nextNodes

        return rslt


root = TreeNode(6)
root.create_tree({
    6: (7, 8),
    7: (2, 10),
    2: (9, None),
    10: (1, 4),
    8: (11, 3),
    3: (None, 5)
})

print(Solution().sumEvenGrandparent(root))
