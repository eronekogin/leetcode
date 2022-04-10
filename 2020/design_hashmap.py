"""
https://leetcode.com/problems/design-hashmap/
"""


class ListNode:

    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._SIZE = 997  # Pick a prime number for hashing.
        self._list = [ListNode(None, None)] * self._SIZE

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        currNode = self._list[key % self._SIZE]
        while currNode.key != key and currNode.next:
            currNode = currNode.next

        if currNode.key == key:
            currNode.val = value
        else:
            currNode.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key.
        """
        currNode = self._list[key % self._SIZE]
        while currNode.key != key and currNode.next:
            currNode = currNode.next

        if currNode.key == key:
            return currNode.val
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map
        contains a mapping for the key.
        """
        prevNode, currNode = None, self._list[key % self._SIZE]
        while currNode.key != key and currNode.next:
            prevNode, currNode = currNode, currNode.next

        if currNode.key == key:
            prevNode.next = currNode.next
