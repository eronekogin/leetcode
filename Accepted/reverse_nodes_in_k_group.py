"""
https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

from test_helper import ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fakeHead = ListNode(None)
        fakeHead.next = l = r = head
        jump, cnt = fakeHead, 0

        while True:
            cnt = 0

            while r and cnt < k:  # Advance r until it points to Node(k+1).
                cnt += 1
                r = r.next

            if cnt == k:  # List is long enough to hold a k group.
                pre, curr = r, l

                for _ in range(k):  # Swap k times to reverse the k group.
                    """   
                    It reverses each node by cutting it from the k group,
                    then pre-append it with the rest of the list 
                    after the k group.

                    Each loop cuts one node starting from the last node in the
                    k group to the first node.

                    For example:
                        Initiallly:
                            k = 3
                            pre = 4 -> None
                            curr = 1 -> 2 -> 3 -> 4 -> None
                        Round 0:
                            pre = 1 -> 4 -> None
                            curr = 2 -> 3 -> 4 -> None
                        Round 1:
                            pre = 2 -> 1 -> 4 -> None
                            curr = 3 -> 4 -> None
                        Round 2:
                            pre = 3 -> 2 -> 1 -> 4 -> None
                            curr = 4 -> None
                        Now the nodes in the k group is reversed and stored in
                        pre.
                    """
                    temp = curr.next  # Store curr.next for later reference.
                    curr.next = pre  # Pre-append current node to the remain.
                    pre = curr  # Move remain pointer to the current node.
                    curr = temp  # Move current node to the previous next node.

                jump.next = pre  # Append the reversed node list to fakeHead.
                jump = l  # Move jump to the end point of the current k group.
                l = r  # Set l to the first item in the next k group.
            else:  # List is exhausted.
                return fakeHead.next


x = ListNode(None)
print(Solution().reverseKGroup(x.create_node_list(1, 5), 3))
