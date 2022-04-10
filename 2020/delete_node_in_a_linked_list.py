"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


from test_helper import ListNode


class Solution:
    def deleteNode(self, node: ListNode):
        node.val = node.next.val
        node.next = node.next.next
