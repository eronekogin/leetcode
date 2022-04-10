"""
https://leetcode.com/problems/remove-linked-list-elements/
"""


from test_helper import ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        newHead = preHead = ListNode(None)
        newHead.next = currHead = head
        while currHead:
            if currHead.val == val:
                preHead.next = currHead.next
            else:
                preHead = preHead.next

            currHead = currHead.next

        return newHead.next
