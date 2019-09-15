"""
https://leetcode.com/problems/reverse-linked-list-ii/
"""

from test_helper import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Presumption: 1 <= m <= n <= length of the list.
        rslt = preNode = ListNode(0)
        preNode.next = currNode = head
        cnt = 1
        while cnt < m:  # Move to the Node m.
            preNode, currNode = preNode.next, currNode.next
            cnt += 1

        tailNode, nextNode = currNode, currNode.next
        tailNode.next = None
        while cnt < n:  # Move to the Node n.
            tempNode = nextNode.next
            nextNode.next = currNode
            currNode = nextNode
            nextNode = tempNode
            cnt += 1

        tailNode.next = nextNode
        preNode.next = currNode
        return rslt.next


print(Solution().reverseBetween(ListNode(0).create_node_list(
    givenList=[1]), 1, 1))
