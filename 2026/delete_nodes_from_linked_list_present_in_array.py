"""
https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/description/
"""

from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def modified_list(self, nums: list[int], head: ListNode) -> ListNode:
        """
        modified list
        """
        root = ListNode(0)
        root.next = head
        candidates = set(nums)
        curr = root

        while curr.next:
            if curr.next.val in candidates:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return root.next
