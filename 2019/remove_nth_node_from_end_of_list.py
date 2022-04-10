"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from test_helper import ListNode


class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        refDict = {}
        cnt = 0
        fakeHead = ListNode(None)
        fakeHead.next = head

        while fakeHead is not None:
            cnt += 1
            refDict[cnt] = fakeHead
            fakeHead = fakeHead.next

        # When list is too short, return the original list head directly.
        if cnt > n:
            # The node to be deleted is stored at refDict[cnt - n + 1].
            refDict[cnt - n].next = refDict.get(cnt - n + 2)

        return refDict[1].next


x = ListNode(None).create_node_list(1, 2)
print('Original List:')
x.print_node_list()
offset = 1
print('Removing {0}th node from the end of the list...'.format(offset))
print('Updated List:')
y = Solution().removeNthFromEnd(x, offset)
if y is not None:
    y.print_node_list()
else:
    print(y)
