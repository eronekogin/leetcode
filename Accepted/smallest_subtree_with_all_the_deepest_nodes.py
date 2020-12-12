"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
"""


from test_helper import TreeNode


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        nextNodes, parents = [root], {}
        while nextNodes:  # Scan from top to down.
            currNodes, nextNodes = nextNodes, []
            for parent in currNodes:
                for child in [parent.left, parent.right]:
                    if child:
                        nextNodes.append(child)
                        parents[child] = parent

        if len(currNodes) == 1:  # Only 1 deepest node found.
            return currNodes[0]

        while len(currNodes) > 1:  # More then 1 deepest nodes found.
            # Scan from down to top to find their common parent.
            currNodes = {parents[node] for node in currNodes}

        return currNodes.pop()
