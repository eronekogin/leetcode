"""
https://leetcode.com/problems/linked-list-cycle/
"""


from test_helper import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        Use two pointers to reduce the space to O(1).
        """
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:  # Fast reaches the end.
                return False

            # Just make sure fast is running at least 2 steps before slow
            # so that they will eventually meet when there is a cycle.
            slow = slow.next
            fast = fast.next.next

        return True
