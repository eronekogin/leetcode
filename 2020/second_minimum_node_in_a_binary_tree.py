"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
"""


from test_helper import TreeNode


from collections import deque


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        queue = deque([root])
        rslt, minVal = float('inf'), root.val
        while queue:
            currNode = queue.popleft()
            if currNode.val > minVal:
                # The minimum value of the sub tree rooted by the current node
                # is already greater than the minimum value, which means we
                # cannot find a better candidate by scanning the remaining
                # parts of the sub tree. So we simply skip it during the bfs
                # process.
                rslt = min(rslt, currNode.val)
            elif currNode.left:  # The current node is not a leaf.
                queue.append(currNode.left)
                queue.append(currNode.right)

        if rslt == float('inf'):  # All the values in the tree are the same.
            return -1

        return rslt
