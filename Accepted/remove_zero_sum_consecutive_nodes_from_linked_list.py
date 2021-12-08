"""
https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
"""


from test_helper import ListNode


class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        memo: dict[int, ListNode] = {}
        memo[0] = dummyHead = ListNode(0)
        dummyHead.next = head

        # Calculate the prefix sums.
        currHead, currSum = head, 0
        while currHead:
            currSum += currHead.val
            memo[currSum] = currHead
            currHead = currHead.next

        # Merge all nodes with the same prefix sum.
        currHead, currSum = dummyHead, 0
        while currHead:
            currSum += currHead.val
            currHead.next = memo[currSum].next
            currHead = currHead.next

        return dummyHead.next


head = ListNode(None).create_node_list(
    givenList=[1, 3, 2, -3, -2, 5, 5, -5, 1])
Solution().removeZeroSumSublists(head).print_single_list()
