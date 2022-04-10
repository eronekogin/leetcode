"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

from test_helper import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        rslt = preNode = ListNode(0)
        preNode.next = currNode = head
        while currNode and currNode.next:
            if currNode.val == currNode.next.val:
                currNode = currNode.next
                while currNode and currNode.next and \
                        currNode.val == currNode.next.val:
                    currNode = currNode.next

                preNode.next = currNode = currNode.next
            else:
                preNode = preNode.next
                currNode = currNode.next

        return rslt.next


a = ListNode(0).create_node_list(givenList=[1, 1])
print(Solution().deleteDuplicates(a))
