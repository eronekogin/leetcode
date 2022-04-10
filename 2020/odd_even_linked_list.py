"""
https://leetcode.com/problems/odd-even-linked-list/
"""


from test_helper import ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        oddTail = head
        evenHead = evenTail = head.next
        while evenTail and evenTail.next:
            oddTail.next = evenTail.next
            oddTail = oddTail.next
            evenTail.next = oddTail.next
            evenTail = evenTail.next

        oddTail.next = evenHead
        return head
