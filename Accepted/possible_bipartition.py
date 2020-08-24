"""
https://leetcode.com/problems/possible-bipartition/
"""


from typing import List
from collections import defaultdict, deque


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if not dislikes:
            return True

        memo = defaultdict(list)  # number: dislikes list
        visited = {}  # number: color
        for k, v in dislikes:
            memo[k].append(v)
            memo[v].append(k)

        for num in memo:
            if num not in visited:
                queue = deque([(num, 1)])
                while queue:
                    curr, color = queue.popleft()
                    if curr not in visited:
                        visited[curr] = color
                        for neighbor in memo[curr]:
                            queue.append((neighbor, -color))

                    if visited[curr] != color:
                        return False

        return True
