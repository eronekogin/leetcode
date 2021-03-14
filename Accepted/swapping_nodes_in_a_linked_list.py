"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""


from test_helper import ListNode


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        currNode, rKthNode = head, None
        cnt = 0
        kthNode = None
        while currNode:
            if rKthNode:
                rKthNode = rKthNode.next

            cnt += 1
            if cnt == k:
                rKthNode = head
                kthNode = currNode

            currNode = currNode.next

        kthNode.val, rKthNode.val = rKthNode.val, kthNode.val
        return head


head = ListNode(1)
print(Solution().swapNodes(head, 1))
