"""
https://leetcode.com/problems/design-circular-deque/
"""


class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here.
        Set the size of the deque to be k.
        """
        self.size = k
        self._tail = None
        self._cnt = 0

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self._tail = ListNode(value)
            self._tail.next = self._tail
            self._cnt = 1
        else:
            preHead = self._tail.next
            self._tail.next = ListNode(value)
            self._tail.next.next = preHead
            preHead.prev = self._tail.next
            self._cnt += 1

        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self._tail = ListNode(value)
            self._tail.next = self._tail
            self._cnt = 1
        else:
            preHead = self._tail.next
            self._tail.next = ListNode(value)
            self._tail.next.prev = self._tail
            self._tail = self._tail.next
            self._tail.next = preHead
            self._cnt += 1

        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self._cnt == 1:
            self._tail = None
            self._cnt = 0
        else:
            self._tail.next = self._tail.next.next
            self._tail.next.prev = None
            self._cnt -= 1

        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self._cnt == 1:
            self._tail = None
            self._cnt = 0
        else:
            preTail = self._tail.prev
            preTail.next = self._tail.next
            self._tail = preTail
            self._cnt -= 1

        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1

        return self._tail.next.val

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1

        return self._tail.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not self._cnt

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._cnt == self.size
