"""
https://leetcode.com/problems/all-oone-data-structure/
"""


from collections import defaultdict


class DoublyLinkedListNode:
    """
    Class for a node in a doubly linked list.
    """

    def __init__(self):
        self._keys = set()
        self.prev = None
        self.next = None

    def add_key(self, key: str) -> None:
        """
        Add a key to the current node's key set.
        """
        self._keys.add(key)

    def remove_key(self, key: str) -> None:
        """
        Remove a key from the current node's key set.
        """
        self._keys.remove(key)

    def get_a_key(self) -> str:
        """
        Get an arbitary key from the node's key set.
        """
        rslt = None

        if self._keys:
            rslt = self._keys.pop()
            self._keys.add(rslt)

        return rslt

    def has_no_key(self) -> bool:
        """
        Check if the current node's key set is empty.
        """
        return len(self._keys) == 0


class DoublyLinkedList:
    """
    Class for a double linked list.
    """

    def __init__(self):
        self._head = DoublyLinkedListNode()
        self._tail = DoublyLinkedListNode()
        self._head.next = self._tail
        self._tail.prev = self._head

    def insert_after(
            self, targetNode: DoublyLinkedListNode) -> DoublyLinkedListNode:
        """
        Insert a new node after the target node and return the new node.
        """
        newNode = DoublyLinkedListNode()
        targetNode.next, newNode.next = newNode, targetNode.next
        newNode.next.prev, newNode.prev = newNode, targetNode
        return newNode

    def insert_before(
            self, targetNode: DoublyLinkedListNode) -> DoublyLinkedListNode:
        """
        Insert a new node before the target node and return the new node.
        """
        return self.insert_after(targetNode.prev)

    def remove(self, targetNode: DoublyLinkedListNode) -> None:
        """
        Remove the target node from the current list.
        """
        targetNode.prev.next = targetNode.next
        targetNode.next.prev = targetNode.prev

    def get_head(self) -> DoublyLinkedListNode:
        """
        Get the actual head of the current list.
        """
        return self._head.next

    def get_tail(self) -> DoublyLinkedListNode:
        """
        Get the actual tail of the current list.
        """
        return self._tail.prev

    def get_sentinel_head(self) -> DoublyLinkedListNode:
        """
        Get the sentinel head of the current list.
        """
        return self._head


class AllOne:
    """
    Class for the problem's solution. It's easy to find out that we could use
    dictionary to increase or decrese the frequency of the keys but dicitonary 
    is not good enough when trying to search for the keys with the maximum or 
    the minimum frequency. In order to do that we create a double linked list 
    with each node as an indicator of a unique frequency. Then all the keys
    having the same frequency will be added to the target node's key set.

    The reason to use double linked list is that the delete or insert a new
    node at a random position is O(1), which is quite fast.
    """

    def __init__(self):
        self._dll = DoublyLinkedList()
        self._key_memo = defaultdict(int)  # {key: val}
        # {frequency: double linked list node}
        self._freq_memo = {0: self._dll.get_sentinel_head()}

    def _remove_key_in_prev_freq_node(self, key: str, prevFreq: int) -> None:
        """
        1. Remove the key from the doubly linked list node associated with
            the previous frequency.

        2. If the node's key set is empty after step 1, remove the node from
            the current list.
        """
        targetNode = self._freq_memo[prevFreq]
        targetNode.remove_key(key)
        if targetNode.has_no_key():
            self._dll.remove(targetNode)
            self._freq_memo.pop(prevFreq)

    def inc(self, key: str) -> None:
        """
        Set the key's value to 1 if the key does not exist, otherwise increase
        its value by 1.
        """
        self._key_memo[key] += 1
        currFreq = self._key_memo[key]
        prevFreq = currFreq - 1
        if currFreq not in self._freq_memo:
            # Add a new node to the current linked list after the node
            # associated with the prev frequency to indicate the current
            # frequcy. Then add it to the frequency memo as well.
            self._freq_memo[currFreq] = self._dll.insert_after(
                self._freq_memo[prevFreq])

        self._freq_memo[currFreq].add_key(key)
        if prevFreq:
            self._remove_key_in_prev_freq_node(key, prevFreq)

    def dec(self, key: str) -> None:
        """
        Decrease an existing key's value by 1. If the current value is zero,
        remove the key.
        """
        if key in self._key_memo:
            self._key_memo[key] -= 1
            currFreq = self._key_memo[key]
            prevFreq = currFreq + 1

            if currFreq == 0:
                self._key_memo.pop(key)

            if currFreq not in self._freq_memo:
                # Add a new node to the current linked list before the node
                # associated with the prev frequency to indicate the current
                # frequcy. Then add it to the frequency memo as well.
                self._freq_memo[currFreq] = self._dll.insert_before(
                    self._freq_memo[prevFreq])

            self._freq_memo[currFreq].add_key(key)
            self._remove_key_in_prev_freq_node(key, prevFreq)

    def getMaxKey(self) -> str:
        """
        Get the key with maximum frequency. If there is not any, return ''.
        """
        return self._dll.get_tail().get_a_key() or ''

    def getMinKey(self) -> str:
        """
        Get the key with minimum frequency. If there is not any, return ''.
        """
        return self._dll.get_head().get_a_key() or ''


a = AllOne()
a.dec('Hello')
a.getMaxKey()
