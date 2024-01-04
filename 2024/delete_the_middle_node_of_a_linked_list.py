"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def delete_middle(self, head: ListNode) -> ListNode | None:
        """
        delete_middle
        """
        # Count total number of nodes.
        curr_node = head
        n = 0
        while curr_node:
            n += 1
            curr_node = curr_node.next

        if n == 1:
            return None

        m = n >> 1
        cnt = -1
        curr_node = prev_node = head
        while curr_node:
            cnt += 1
            if cnt == m:  # Found the middle node.
                prev_node.next = curr_node.next
                break

            prev_node = curr_node
            curr_node = curr_node.next

        return head
