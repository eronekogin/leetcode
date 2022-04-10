"""
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""


from test_helper import DoublyLinkedListNode


class Solution:
    def flatten(self, head: DoublyLinkedListNode) -> DoublyLinkedListNode:
        currNode = head
        stack = []
        while currNode or stack:
            if currNode.child:  # Has child
                stack.append(currNode)
                currNode = currNode.child  # Process its child first.
            elif not currNode.next:  # Has no next node.
                while stack and not stack[-1].next:
                    # Flat previous node and its child.
                    prevNode = stack.pop()
                    prevNode.child.prev = prevNode
                    prevNode.next = prevNode.child
                    prevNode.child = None

                if stack:  # Still contain parent node.
                    prevNode = stack.pop()
                    nextNode = prevNode.next

                    # Flat previous node and its child.
                    prevNode.child.prev = prevNode
                    prevNode.next = prevNode.child
                    prevNode.child = None

                    # Flat the current node and the next node.
                    nextNode.prev = currNode
                    currNode.next = nextNode

                currNode = currNode.next
            else:  # Has next node.
                currNode = currNode.next

        return head
