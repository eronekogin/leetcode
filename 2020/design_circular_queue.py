"""
https://leetcode.com/problems/design-circular-queue/
"""


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __repr__(self) -> str:
        return str(self.val)


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self._size = k
        self._curr = 0
        self._rear = None

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue.
        Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self._rear is None:
            self._rear = ListNode(value)
            self._rear.next = self._rear
        else:
            temp = self._rear.next
            self._rear.next = ListNode(value)
            self._rear.next.next = temp
            self._rear = self._rear.next

        self._curr += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue.
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        if self._rear.next == self._rear:
            self._rear = None
        else:
            self._rear.next = self._rear.next.next

        self._curr -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1

        return self._rear.next.val

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1

        return self._rear.val

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self._curr == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self._curr == self._size


q = MyCircularQueue(3)
q.enQueue(1)
q.deQueue()
