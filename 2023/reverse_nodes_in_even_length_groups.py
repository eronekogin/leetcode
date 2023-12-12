"""
https://leetcode.com/problems/reverse-nodes-in-even-length-groups/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def reverse_even_length_groups(self, head: ListNode) -> ListNode:
        """
        reverse_even_length_groups
        """
        prev = head
        count = 2
        while prev.next:
            curr, n = prev, 0
            while n < count and curr.next:
                curr = curr.next
                n += 1

            if n % 2 == 0:  # even
                curr = prev.next
                prev.next, curr.next = self.reverse(curr, n)

            prev = curr
            count += 1

        return head

    def reverse(self, node, k):
        """
        reverse
        """
        prev = None
        for _ in range(k):
            node.next, prev, node = prev, node, node.next
        return prev, node
