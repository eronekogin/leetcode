"""
https://leetcode.com/problems/robot-collisions/description/
"""


class Solution:
    """
    Solution
    """

    def survived_robots_healths(
        self,
        positions: list[int],
        healths: list[int],
        directions: str
    ) -> list[int]:
        """
        survive robots healths
        """
        memo = [
            (p, i)
            for i, p in enumerate(positions)
        ]

        memo.sort(key=lambda x: x[0])
        stack: list[int] = []

        for _, i in memo:
            d = directions[i]
            h = healths[i]
            if (
                not stack or
                directions[stack[-1]] == d or
                (directions[stack[-1]] == 'L' and d == 'R')
            ):
                stack.append(i)
                continue

            while stack and directions[stack[-1]] != d:
                if healths[stack[-1]] < h:
                    stack.pop()
                    h -= 1
                elif healths[stack[-1]] == h:
                    stack.pop()
                    h = 0
                    break
                else:
                    healths[stack[-1]] -= 1
                    h = 0
                    break

            healths[i] = h
            if h > 0:
                stack.append(i)

        stack.sort()
        return [healths[i] for i in stack]


print(Solution().survived_robots_healths(
    positions=[3, 5, 2, 6], healths=[10, 10, 15, 12], directions="RLRL"))
