"""
https://leetcode.com/problems/partition-list/
"""

from test_helper import ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        lHead = l = ListNode(0)
        rHead = r = ListNode(0)
        currNode = head
        while currNode:
            if currNode.val < x:
                l.next = currNode
                l = l.next
            else:
                r.next = currNode
                r = r.next

            currNode = currNode.next

        # Note that the current r should be the last node in the new list.
        r.next = None
        l.next = rHead.next
        return lHead.next


head = ListNode(0).create_node_list(givenList=[1, 4, 3, 2, 5, 2])
print(Solution().partition(head, 3))
