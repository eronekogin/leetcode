"""
https://leetcode.com/problems/design-linked-list/
"""


from typing import List


class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None
        self._tail = None
        self._currLen = 0

    def _search(self, index: int) -> List[ListNode]:
        prevNode, currNode = None, self._head
        for _ in range(index):
            prevNode, currNode = currNode, currNode.next

        return [prevNode, currNode]

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.
        """
        if index < 0 or index >= self._currLen:
            return -1

        return self._search(index)[1].val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of
        the linked list.
        """
        if self._currLen:
            newNode = ListNode(val)
            newNode.next = self._head
            self._head = newNode
        else:
            self._head = self._tail = ListNode(val)

        self._currLen += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self._currLen:
            self._tail.next = ListNode(val)
            self._tail = self._tail.next
        else:
            self._head = self._tail = ListNode(val)

        self._currLen += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be
        appended to the end of linked list. If index is greater than
        the length, the node will not be inserted.
        """
        if index < 0 or index > self._currLen:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self._currLen:
            self.addAtTail(val)
        else:
            prevNode, currNode = self._search(index)
            newNode = ListNode(val)
            prevNode.next, newNode.next = newNode, currNode
            self._currLen += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self._currLen:
            if index == 0:  # Delete at head.
                self._head = self._head.next
            else:
                prevNode, currNode = self._search(index)
                prevNode.next = currNode.next
                if index == self._currLen - 1:  # Delete at tail.
                    self._tail = prevNode

            self._currLen -= 1
            if not self._currLen:  # All the nodes have been deleted now.
                self._head = self._tail = None


m = MyLinkedList()
m.addAtIndex(0, 10)
m.addAtIndex(0, 20)
m.addAtIndex(0, 30)
