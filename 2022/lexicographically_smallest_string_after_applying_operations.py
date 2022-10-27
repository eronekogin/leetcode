"""
https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
"""


from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q = deque([s])
        visited = {s}
        minStr = s
        while q:
            curr = q.popleft()
            if curr < minStr:
                minStr = curr

            # Perform add.
            nextStr = ''.join(
                [
                    str((int(c) + a) % 10) if i & 1 else c
                    for i, c in enumerate(curr)
                ]
            )
            if nextStr not in visited:
                visited.add(nextStr)
                q.append(nextStr)

            # Perform rotate.
            nextStr = curr[-b:] + curr[:-b]
            if nextStr not in visited:
                visited.add(nextStr)
                q.append(nextStr)

        return minStr
