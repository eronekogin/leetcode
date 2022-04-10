from test_helper import TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''

        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not left and not right:
            return str(t.val)
        elif not left:
            return '{0}()({1})'.format(t.val, right)
        elif not right:
            return '{0}({1})'.format(t.val, left)
        else:
            return '{0}({1})({2})'.format(t.val, left, right)


root = TreeNode(1)
root.create_tree({
    1: (2, 3),
    2: (None, 4)
})
print(Solution().tree2str(root))
