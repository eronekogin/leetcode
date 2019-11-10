"""
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

from test_helper import ListNode


class Solution(object):
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:  # Either list is empty.
            return None

        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = headB if nodeA is None else nodeA.next
            nodeB = headA if nodeB is None else nodeB.next

        return nodeA
