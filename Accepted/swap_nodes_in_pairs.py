"""
https://leetcode.com/problems/swap-nodes-in-pairs/
"""

from test_helper import ListNode


class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        fakeHead = ListNode(None)
        pre = fakeHead
        pre.next = head

        while pre.next and pre.next.next:
            n1 = pre.next
            n2 = n1.next
            pre.next, n1.next, n2.next = n2, n2.next, n1
            pre = n1

        return fakeHead.next


l = ListNode(None).create_node_list(givenList=[1, 2, 3, 4])
print('The original list is:')
print(l)
print('The swapped list is:')
print(Solution().swapPairs(l))
