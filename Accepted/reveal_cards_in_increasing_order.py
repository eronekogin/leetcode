"""
https://leetcode.com/problems/reveal-cards-in-increasing-order/
"""


from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: list[int]) -> list[int]:
        """
        Simulate the card operations on the index, then assign the value to
        each index.
        """
        N = len(deck)
        sortedIndexes = deque(range(N))
        rslt = [None] * N
        for card in sorted(deck):
            rslt[sortedIndexes.popleft()] = card
            if sortedIndexes:
                sortedIndexes.append(sortedIndexes.popleft())

        return rslt
