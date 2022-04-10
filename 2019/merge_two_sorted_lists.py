"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""

from test_helper import ListNode


class Solution:
    def mergeTwoLists(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        dumyHead = ListNode(None)
        temp = dumyHead

        while l1 and l2:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next

        if l1:
            temp.next = l1

        if l2:
            temp.next = l2

        return dumyHead.next
