"""
https://leetcode.com/problems/add-two-numbers/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        initNode = ListNode(None)
        currNode = initNode
        addOne = 0

        while l1 or l2:
            x = addOne

            if l1:
                x += l1.val
                l1 = l1.next

            if l2:
                x += l2.val
                l2 = l2.next

            currNode.next = ListNode(x % 10)
            currNode = currNode.next
            addOne = x // 10

        if addOne:
            currNode.next = ListNode(1)

        return initNode.next
