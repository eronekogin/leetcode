"""
https://leetcode.com/problems/defuse-the-bomb/description/
"""


class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        N = len(code)
        newCode = [0] * N
        if k == 0:
            return newCode

        direction = 1 if k > 0 else -1
        maxOffset = abs(k) + 1
        for i in range(N):
            newCode[i] = sum(
                code[(i + j * direction) % N]
                for j in range(1, maxOffset)
            )

        return newCode
