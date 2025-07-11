"""
https://leetcode.com/problems/find-the-losers-of-the-circular-game/description/
"""


class Solution:
    """
    Solution
    """

    def circular_game_losers(self, n: int, k: int) -> list[int]:
        """
        circular game losers
        """
        visited = [False] * n
        r = 0
        curr = 0
        while not visited[curr]:
            visited[curr] = True
            r += 1
            curr = (curr + k * r) % n

        return [
            i + 1
            for i, x in enumerate(visited)
            if not x
        ]


print(Solution().circular_game_losers(5, 2))
