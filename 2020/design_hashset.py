"""
https://leetcode.com/problems/design-hashset/
"""


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.size = 10_000
        self.items = [None] * self.size

    def _get_node(self, key: int) -> ListNode:
        preNode, currNode = None, self.items[key % self.size]
        while currNode:
            if currNode.val == key:
                break

            preNode, currNode = currNode, currNode.next

        return (preNode, currNode)

    def add(self, key: int) -> None:
        preNode, currNode = self._get_node(key)
        if not currNode:
            if not preNode:
                self.items[key % self.size] = ListNode(key)
            else:
                preNode.next = ListNode(key)

    def remove(self, key: int) -> None:
        preNode, currNode = self._get_node(key)
        if currNode:
            if not preNode:
                self.items[key % self.size] = currNode.next
            else:
                preNode.next = currNode.next

    def contains(self, key: int) -> bool:
        return self._get_node(key)[1] != None
