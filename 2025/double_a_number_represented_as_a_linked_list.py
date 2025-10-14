"""
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def double_it(self, head: ListNode) -> ListNode:
        """
        double it
        """
        if head.val > 4:
            new_head = ListNode(0)
            new_head.next = head
        else:
            new_head = head

        curr = new_head
        while curr:
            curr.val = (curr.val << 1) % 10
            if curr.next and curr.next.val > 4:
                curr.val += 1

            curr = curr.next

        return new_head


head_node = ListNode(0)
print(Solution().double_it(head_node))
