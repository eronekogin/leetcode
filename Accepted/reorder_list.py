"""
https://leetcode.com/problems/reorder-list/
"""


from test_helper import ListNode


class Solution:
    def reorderList(self, head: ListNode):
        if not head or not head.next or not head.next.next:
            # List contains no more than 2 nodes.
            return

        # Find the middle node of the list first.
        middleNode, tailNode = head, head.next
        while tailNode and tailNode.next:
            middleNode = middleNode.next
            tailNode = tailNode.next.next

        currNode, nextNode = middleNode.next, middleNode.next.next

        # Cut the list at the middle point.
        middleNode.next, currNode.next = None, None

        # Reverse the half list starting at the currNode.
        while nextNode:
            tempNode = nextNode.next
            nextNode.next = currNode
            currNode = nextNode
            nextNode = tempNode

        # Merge the two lists.
        currNode, nextNode = head, currNode
        while currNode:
            tempNode = currNode.next
            currNode.next = nextNode
            currNode = nextNode
            nextNode = tempNode


root = ListNode(None).create_node_list(1, 5)
Solution().reorderList(root)
print(root.print_single_list())
