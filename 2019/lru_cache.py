"""
https://leetcode.com/problems/lru-cache/
"""


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.items = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        value = self.items[key]
        del self.items[key]
        self.items[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            del self.items[key]

        if len(self.items) == self.capacity:  # Exceed the capacity.
            self.items.popitem(last=False)  # Pop the lru item.

        self.items[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
