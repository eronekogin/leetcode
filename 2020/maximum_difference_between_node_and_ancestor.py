"""
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""


from test_helper import TreeNode


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def check(curr: TreeNode, currMax: int, currMin: int) -> int:
            if not curr:
                return currMax - currMin

            nextMax = max(currMax, curr.val)
            nextMin = min(currMin, curr.val)
            return max(
                check(curr.left, nextMax, nextMin),
                check(curr.right, nextMax, nextMin))

        return check(root, root.val, root.val)


root = TreeNode(8)
root.create_tree({
    8: (3, 10),
    3: (1, 6),
    6: (4, 7),
    10: (None, 14),
    14: (None, 13)
})
print(Solution().maxAncestorDiff(root))
