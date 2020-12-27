"""
https://leetcode.com/problems/jump-game-iv/
"""


from typing import List

from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr)
        if N <= 1:
            return 0

        memo = defaultdict(list)
        for currIdx, currNum in enumerate(arr):
            memo[currNum].append(currIdx)

        queue = deque([(0, 0)])
        visitedIdxes, visitedNumbers = set(), set()
        while queue:
            currJumps, currIdx = queue.popleft()
            if currIdx == N - 1:
                return currJumps

            # Jump to neighbors.
            for jumpIdx in [currIdx - 1, currIdx + 1]:
                if 0 <= jumpIdx < N and jumpIdx not in visitedIdxes:
                    visitedIdxes.add(jumpIdx)
                    queue.append((currJumps + 1, jumpIdx))

            # Jump to indexes having the same value.
            currNum = arr[currIdx]
            if currNum not in visitedNumbers:
                visitedNumbers.add(currNum)
                for jumpIdx in memo[currNum]:
                    if jumpIdx not in visitedIdxes:
                        visitedIdxes.add(jumpIdx)
                        queue.append((currJumps + 1, jumpIdx))


print(Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
