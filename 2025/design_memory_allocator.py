"""
https://leetcode.com/problems/design-memory-allocator/description/
"""


class Allocator:
    """
    Allocator
    """

    def __init__(self, n: int):
        self.free = chr(0)
        self.memory = self.free * n

    def allocate(self, size: int, mid: int) -> int:
        """
        allocate
        """
        i = self.memory.find(self.free * size)
        if i != -1:
            self.memory = (
                self.memory[:i] +
                chr(mid) * size +
                self.memory[i + size:]
            )

        return i

    def free_memory(self, mid: int) -> int:
        """
        free memory
        """
        cnt = self.memory.count(chr(mid))
        self.memory = self.memory.replace(chr(mid), self.free)
        return cnt
