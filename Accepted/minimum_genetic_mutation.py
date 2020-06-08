"""
https://leetcode.com/problems/minimum-genetic-mutation/
"""


from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        Use BFS solution.
        """
        mutations = set(bank)
        queue = deque([(start, 0)])
        while queue:
            currStr, currSteps = queue.popleft()
            if currStr == end:
                return currSteps

            for i in range(len(currStr)):
                for c in 'ACGT':
                    mutation = currStr[:i] + c + currStr[i + 1:]
                    if mutation in mutations:
                        queue.append((mutation, currSteps + 1))
                        # Try to find the minimum steps of mutations. So no
                        # need to consider the duplication cases.
                        mutations.remove(mutation)

        return -1  # Not found.
