"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

See the approch 3 in the link below for a detail example:

https://leetcode.com/articles/convert-sorted-list-to-binary-search-tree/?page=2
"""


from test_helper import ListNode, TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """
        Storing all the values in the linked list will take O(n) space while
        using bottom-up solution will reduce it to O(logn).
        """
        if not head:  # Empty Tree
            return None

        #  Get linked list size first.
        n, self.currNodeInList = -1, head
        while self.currNodeInList:
            n += 1
            self.currNodeInList = self.currNodeInList.next

        self.currNodeInList = head
        return self.create_tree(0, n)

    def create_tree(self, l: int, r: int) -> TreeNode:
        if l > r:
            return None

        m = (l + r) // 2

        left = self.create_tree(l, m - 1)

        root = TreeNode(self.currNodeInList.val)
        root.left = left

        self.currNodeInList = self.currNodeInList.next

        root.right = self.create_tree(m + 1, r)

        return root
