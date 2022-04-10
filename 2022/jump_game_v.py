"""
https://leetcode.com/problems/jump-game-v/
"""


from collections import defaultdict
from typing import Iterator


class Solution:
    def maxJumps(self, arr: list[int], d: int) -> int:
        def jump(iterator: Iterator[int]) -> None:
            stack = []
            for dst in iterator:
                while stack and arr[stack[-1]] < arr[dst]:
                    src = stack.pop()
                    if abs(src - dst) <= d:
                        graph[src].append(dst)

                stack.append(dst)

        def find_path(start: int) -> int:
            if start not in memo:
                memo[start] = 1 + max(
                    [find_path(dst) for dst in graph[start]] or [0]
                )

            return memo[start]

        N = len(arr)
        graph = defaultdict(list)
        memo = {}

        # Initialize graph by jumping from 0 to N, the from N to 0.
        jump(range(N))
        jump(reversed(range(N)))

        # Then use dfs to find the longest path in graph.
        return max(find_path(i) for i in range(N))
