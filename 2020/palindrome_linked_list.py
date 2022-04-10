"""
https://leetcode.com/problems/palindrome-linked-list/
"""


from test_helper import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        reverse = None
        while fast and fast.next:
            fast = fast.next.next

            # Reverse the first half of the list.
            nextSlow = slow.next
            slow.next = reverse
            reverse, slow = slow, nextSlow

        if fast:  # The total nodes in the input list is and odd number.
            slow = slow.next  # Make left and right side equal length.

        # Now walk towards both sides to determine if it is a palindrome list.
        while reverse and reverse.val == slow.val:
            reverse = reverse.next
            slow = slow.next

        return not reverse
