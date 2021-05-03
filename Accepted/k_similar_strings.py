"""
https://leetcode.com/problems/k-similar-strings/
"""


from collections import deque
from typing import Iterator


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        """
        1. Try to make one swap in s1 to make it more similar to s2, then take
            this swapped string as a neighbor node to s1.
        2. Then our goal is to find the shorted path from node s1 to node s2
            from the generated graph.
        3. We could then use BFS to get that path.
        """
        def neighbors(s: str) -> Iterator[str]:
            i = 0
            while s[i] == s2[i]:  # Skip the already swapped chars.
                i += 1

            t = list(s)
            for j in range(i + 1, N):
                # Make a swap.
                if s[j] == s2[i] and s[j] != s2[j]:
                    t[i], t[j] = t[j], t[i]
                    yield ''.join(t)
                    t[i], t[j] = t[j], t[i]

        N = len(s1)
        queue = deque([(s1, 0)])
        visited = {s1}
        while queue:
            s, swapCnt = queue.popleft()
            if s == s2:
                return swapCnt

            swapCnt += 1
            for neighbor in neighbors(s):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, swapCnt))
