"""
https://leetcode.com/problems/add-two-numbers-ii/
"""


from test_helper import ListNode
from typing import List


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Cheat answer: python does not have a limit on integer.
        """
        def get_number(l: ListNode) -> int:
            rslt, curr = 0, l
            while curr:
                rslt = rslt * 10 + curr.val
                curr = curr.next

            return rslt

        n = str(get_number(l1) + get_number(l2))
        dummyHead = currNode = ListNode(None)
        for c in n:
            currNode.next = ListNode(int(c))
            currNode = currNode.next

        return dummyHead.next

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Regular solution using a stack.
        """
        def get_stack(l: ListNode) -> List[int]:
            stack, curr = [], l
            while curr:
                stack.append(curr.val)
                curr = curr.next

            return stack

        s1, s2 = get_stack(l1), get_stack(l2)
        carry, nextNode = 0, None
        while s1 or s2 or carry:
            curr = 0
            if s1:
                curr += s1.pop()

            if s2:
                curr += s2.pop()

            carry, curr = divmod(curr + carry, 10)
            currNode = ListNode(curr)
            currNode.next = nextNode
            nextNode = currNode

        return nextNode
