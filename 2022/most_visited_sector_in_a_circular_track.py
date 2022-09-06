"""
https://leetcode.com/problems/most-visited-sector-in-a-circular-track/
"""


class Solution:
    def mostVisited(self, n: int, rounds: list[int]) -> list[int]:
        cnt: list[int] = [0] * n
        for start, end in zip(rounds, rounds[1:]):
            if start <= end:
                for i in range(start - 1, end - 1):
                    cnt[i] += 1
            else:
                for i in range(start - 1, end + n - 1):
                    cnt[i % n] += 1

        cnt[rounds[-1] - 1] += 1  # Add last sector.
        maxVal = max(cnt)
        return [i + 1 for i, v in enumerate(cnt) if v == maxVal]


print(Solution().mostVisited(2,
                             [2, 1, 2, 1, 2, 1, 2, 1, 2]))
