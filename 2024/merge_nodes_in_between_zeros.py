"""
https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
"""


from test_helper import ListNode


class Solution:
    """
    Solution
    """

    def merge_nodes(self, head: ListNode) -> ListNode:
        """
        merge nodes
        """
        rslt = start = head.next
        while start:
            end = start
            curr_sum = 0
            while end.val != 0:
                curr_sum += end.val
                end = end.next

            start.val = curr_sum
            start.next = end.next
            start = start.next

        return rslt
