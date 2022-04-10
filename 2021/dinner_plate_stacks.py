"""
https://leetcode.com/problems/dinner-plate-stacks/
"""


from heapq import heappush, heappop


class DinnerPlates:

    def __init__(self, capacity: int):
        self.availableIndexes = []
        self.allStacks = []
        self.capacity = capacity

    def push(self, val: int) -> None:
        # Remove the full stack at the top of the heap until the current
        # stack is not full. Notice that the index in the heap might be
        # outside of the current allStacks list as the allStacks list could
        # be reduced to smaller size during pop method.
        while (
            self.availableIndexes
            and self.availableIndexes[0] < len(self.allStacks)
            and len(self.allStacks[self.availableIndexes[0]]) == self.capacity
        ):
            heappop(self.availableIndexes)

        if not self.availableIndexes:  # All full, open a new stack then.
            heappush(self.availableIndexes, len(self.allStacks))

        # If the smallest index in the heap is the same as the total length
        # of all the stacks.
        if self.availableIndexes[0] == len(self.allStacks):
            self.allStacks.append([])

        self.allStacks[self.availableIndexes[0]].append(val)

    def pop(self) -> int:
        # Pop all emtpy stacks at the tail.
        while self.allStacks and not self.allStacks[-1]:
            self.allStacks.pop()

        return self.popAtStack(len(self.allStacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.allStacks) and self.allStacks[index]:
            heappush(self.availableIndexes, index)
            return self.allStacks[index].pop()

        return -1
