"""
https://leetcode.com/problems/jump-game-iv/
"""


from typing import List

from collections import deque, defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        N = len(arr) - 1
        if N <= 0:
            return 0

        # Skip any consecutive numbers in the middle and keep the
        # first and the last duplicate number's index.
        memo = defaultdict(list)
        for currIdx, currNum in enumerate(arr):
            if 0 < currIdx < N and arr[currIdx - 1] == arr[currIdx] and \
                    arr[currIdx + 1] == arr[currIdx]:
                continue

            memo[currNum].append(currIdx)

        queue, visitedIdxes = deque([(0, 0)]), set()
        while queue:
            currJumps, currIdx = queue.popleft()
            if currIdx == N:
                return currJumps

            # Jump to neighbors.
            for jumpIdx in [currIdx - 1, currIdx + 1]:
                if 0 <= jumpIdx <= N and jumpIdx not in visitedIdxes:
                    visitedIdxes.add(jumpIdx)
                    queue.append((currJumps + 1, jumpIdx))

            # Jump to indexes having the same value.
            currNum = arr[currIdx]
            for jumpIdx in memo[currNum]:
                if jumpIdx not in visitedIdxes:
                    visitedIdxes.add(jumpIdx)
                    queue.append((currJumps + 1, jumpIdx))

            memo[currNum] = []  # Prevent being searched again.


print(Solution().minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404]))
