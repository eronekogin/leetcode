"""
https://leetcode.com/problems/reverse-linked-list/
"""


from test_helper import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        preHead, currHead = head, head.next
        preHead.next = None
        while currHead:
            nextHead = currHead.next
            currHead.next = preHead
            preHead, currHead = currHead, nextHead

        return preHead
