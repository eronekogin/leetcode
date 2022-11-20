"""
https://leetcode.com/problems/merge-in-between-linked-lists/
"""


from test_helper import ListNode


class Solution:
    def mergeInBetween(
        self,
        list1: ListNode,
        a: int,
        b: int,
        list2: ListNode
    ) -> ListNode:
        n1 = list1
        cnt = 0
        while cnt + 1 < a:
            n1 = n1.next
            cnt += 1

        start = n1
        while cnt <= b:
            n1 = n1.next
            cnt += 1

        end = n1
        n2 = list2
        start.next = n2
        while n2.next:
            n2 = n2.next

        n2.next = end
        return list1
