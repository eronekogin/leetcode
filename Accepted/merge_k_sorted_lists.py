"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""

from test_helper import ListNode


class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        if not lists:  # Lists is None or empty.
            return None

        interval, total = 1, len(lists)

        while interval < total:
            for i in range(0, total - interval, interval * 2):
                # Merge lists[i] and lists[i + interval]
                # and store results into lists[i].
                fakeHead = ListNode(None)
                tempNode = fakeHead
                l1, l2 = lists[i], lists[i + interval]

                while l1 and l2:
                    if l1.val < l2.val:
                        tempNode.next = l1
                        l1 = l1.next
                    else:
                        tempNode.next = l2
                        l2 = l2.next
                    tempNode = tempNode.next

                if l1:
                    tempNode.next = l1

                if l2:
                    tempNode.next = l2

                lists[i] = fakeHead.next  # Store merged list back to lists[i].

            interval *= 2  # Increase interval.

        return lists[0]


x = ListNode(None)
s = Solution()
l1 = x.create_node_list(givenList=[1, 4, 5])
l2 = x.create_node_list(givenList=[1, 3, 4])
l3 = x.create_node_list(givenList=[2, 6])
print('Original list is: ')
for l in [l1, l2, l3]:
    l.print_node_list()
print('Merged list is:')
s.mergeKLists([l1, l2, l3]).print_node_list()
