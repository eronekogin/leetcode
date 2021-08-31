"""
https://leetcode.com/problems/next-greater-node-in-linked-list/
"""


from test_helper import ListNode


class Solution:
    def nextLargerNodes(self, head: ListNode) -> list[int]:
        totalLen = 0
        currNode = head
        while currNode:
            totalLen += 1
            currNode = currNode.next

        rslt = [0] * totalLen
        currNode = head
        stack = []
        i = -1
        while currNode:
            i += 1
            val = currNode.val
            while stack and stack[-1][1] < val:
                rslt[stack.pop()[0]] = val

            stack.append((i, val))
            currNode = currNode.next

        return rslt
