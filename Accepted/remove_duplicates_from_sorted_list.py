"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

from test_helper import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        currNode = head
        while currNode and currNode.next:
            if currNode.val == currNode.next.val:
                currNode.next = currNode.next.next
            else:
                currNode = currNode.next

        return head


head = ListNode(0).create_node_list(givenList=[1, 1, 2])
print(Solution().deleteDuplicates(head))
