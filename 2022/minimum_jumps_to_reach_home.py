"""
https://leetcode.com/problems/minimum-jumps-to-reach-home/
"""


from collections import deque


class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        bound = max(x, *forbidden) + a + b
        queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        blocked: set[tuple[int, int]] = {
            (pos, direction)
            for pos in forbidden for direction in (0, 1)
        }
        while queue:
            pos, steps, isPreviousJumpForward = queue.popleft()
            if pos == x:
                return steps

            if pos > bound or (pos, isPreviousJumpForward) in blocked:
                continue

            blocked.add((pos, isPreviousJumpForward))
            queue.append((pos + a, steps + 1, 1))

            if isPreviousJumpForward and pos > b:
                queue.append((pos - b, steps + 1, 0))

        return -1


print(Solution().minimumJumps([8, 3, 16, 6, 12, 20], 15, 13, 11))
