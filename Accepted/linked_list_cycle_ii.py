"""
https://leetcode.com/problems/linked-list-cycle-ii/
"""


from test_helper import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Suppose we have 2 pointers slow and fast: slow moves one step at a time
        while faster moves 2 steps. 

        Initially fast is at one step further than slow, which in our case 
        slow = head while fast = head.next.

        Suppose at the time they meet slow runs k steps, then fast must
        runs 2k steps. Then based on the below picture we have:

        |----k------|
        |--s1---|
        1 2 3 4 5 6 7 8 9
          |-s2--|---r---|
                |
                start point of the cycle

        1.  (2k - s2) - (k - s1) = n * r while n is how many more cycles the
            fast has run than the slow and r is the length of the cycle.

        2.  Then we have k + s1 - s2 = n * r. Initially we have s1 - s2 = 1,
            and in order to simplify the case we just set n to 1, which means
            the fast will just run 1 more cycle than the slow, then when the
            two pointers meet, the slow was just in his first round of the
            cycle, so the k is what actually showed on the above picture.

        3.  Now we have k + 1 = r. First we try to find where the actual k is.
            Then we reset the slow to the start point of the list while fast
            to the next node of the node k.

        4.  So now the slow has to be moved s1 steps in order to get to the
            start point of the cycle, while the fast is now at k + 1 + s1 - r
            = r + s1 - r = s1, which is also the start point of the cycle. So
            now we have finally found the start point of the cycle.
        """
        if not head or not head.next:
            return None

        # Try to find the meet point when the fast just runs one more cycle.
        # than the slow.
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:  # The fast reaches the end.
                return None

            slow = slow.next
            fast = fast.next.next

        slow, fast = head, fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next

        # Now both the slow and fast points to the cycle start point.
        return slow


print(Solution().detectCycle(ListNode(None).create_cycle_list(
    [3, 2, 0, -4], 1)))
