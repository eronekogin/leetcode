"""
https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/
"""


from math import gcd

from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def insert_greatest_common_divisors(self, head: ListNode) -> ListNode:
        """
        insert greatest common divisors
        """
        curr_node = head
        while curr_node:
            next_node = curr_node.next
            if next_node is None:
                break

            new_node = ListNode(gcd(curr_node.val, next_node.val))
            curr_node.next = new_node
            new_node.next = next_node
            curr_node = next_node

        return head
