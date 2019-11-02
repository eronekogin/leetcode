"""
https://leetcode.com/problems/sort-list/
"""


from test_helper import ListNode


class Solution:
    def _cut_list(self, head: ListNode, n: int) -> ListNode:
        """
        Cut the first n node from head and
        return the head of the remaining list.
        """
        cnt, currNode = 1, head
        while currNode and cnt < n:
            currNode = currNode.next
            cnt += 1

        if not currNode:  # Either emtpy or not enough remaining nodes.
            return None

        newHead = currNode.next
        currNode.next = None  # Cut the list.
        return newHead

    def _merge_list(
            self, h1: ListNode, h2: ListNode, preHead: ListNode) -> ListNode:
        """
        Merge two sorted lists and return the tail of the new list.
        """
        currNode = preHead
        while h1 and h2:
            if h1.val <= h2.val:
                currNode.next, h1 = h1, h1.next
            else:
                currNode.next, h2 = h2, h2.next

            currNode = currNode.next

        # Append the remaining.
        currNode.next = h1 if h1 else h2

        # Go to the tail of the new list.
        while currNode.next:
            currNode = currNode.next

        return currNode

    def sortList(self, head: ListNode) -> ListNode:
        """
        Use bottom-up merge sort to achieve 
        the o(nlogn) runtime and the o(1) space.
        """
        if not head or not head.next:  # Empty or only one node.
            return head

        # Get the total size of the list first.
        n, currNode = 0, head
        while currNode:
            n, currNode = n + 1, currNode.next

        # Keep cutting and merging the sub lists.
        step, dummyHead = 1, ListNode(None)
        dummyHead.next = head
        while step < n:
            currHead, currTail = dummyHead.next, dummyHead
            while currHead:
                leftHead = currHead
                rightHead = self._cut_list(leftHead, step)
                currHead = self._cut_list(rightHead, step)
                currTail = self._merge_list(leftHead, rightHead, currTail)

            step *= 2

        return dummyHead.next


head = ListNode(None).create_node_list(givenList=[6, 5, 4, 3, 2, 1])
print(Solution().sortList(head).print_single_list())
