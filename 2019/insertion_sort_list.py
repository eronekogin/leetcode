"""
https://leetcode.com/problems/insertion-sort-list/
"""


from test_helper import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(None)
        currNode, dummyHead.next, preInsertPos = head, head, dummyHead
        while currNode and currNode.next:
            # The current node always points to the end of the sorted sequece.
            nextVal = currNode.next.val
            if nextVal < currNode.val:
                # The next node needs to be inserted to the current sequence.
                # Try to find the insert position first.
                if nextVal < preInsertPos.next.val:
                    preInsertPos = dummyHead

                while preInsertPos.next and preInsertPos.next.val <= nextVal:
                    preInsertPos = preInsertPos.next

                # Insert the nextNode between preInsertPos
                # and preInsertPos.next.
                newNode = currNode.next
                currNode.next = newNode.next
                newNode.next = preInsertPos.next
                preInsertPos.next = newNode
            else:
                currNode = currNode.next  # Sort the next node.

        return dummyHead.next


head = ListNode(None).create_node_list(givenList=[4, 2, 1, 3])
print(Solution().insertionSortList(head).print_single_list())
