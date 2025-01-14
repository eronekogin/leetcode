"""
https://leetcode.com/problems/remove-nodes-from-linked-list/description/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def remove_nodes(self, head: ListNode) -> ListNode:
        """
        remove nodes
        """
        vals: list[int] = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next

        is_deleted = [False] * len(vals)
        curr_max = vals[-1]
        for i in range(len(vals) - 1, -1, -1):
            if vals[i] < curr_max:
                is_deleted[i] = True
            elif vals[i] > curr_max:
                curr_max = vals[i]

        fake_head = ListNode(-1)
        fake_head.next = head
        prev, curr = fake_head, fake_head.next
        for i, mark in enumerate(is_deleted):
            if mark:
                prev.next = curr = curr.next
            else:
                prev, curr = curr, curr.next

        return fake_head.next
