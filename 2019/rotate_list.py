"""
https://leetcode.com/problems/rotate-list/
"""

from test_helper import ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not k or not head or not head.next:
            return head

        tail = head
        totalNodes, splitPos = 1, k
        while tail.next:  # Count how many nodes in the current list.
            totalNodes += 1
            tail = tail.next

        # Move totalNodes places equals to not move anything.
        splitPos = k % totalNodes
        if splitPos:
            currHead = head
            for _ in range(totalNodes - splitPos):
                preHead = currHead
                currHead = currHead.next

            preHead.next = None
            tail.next = head  # Connect the tail with the head.
            return currHead
        else:
            return head


head = ListNode(0).create_node_list(1, 4)
print(Solution().rotateRight(head, 2))
