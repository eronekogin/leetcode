"""
https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/
"""


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        def dfs(i: int):
            if i == N:
                return all(isUsed)

            if rslt[i] > 0:  # number i is already processed.
                return dfs(i + 1)

            for x in range(n, 0, -1):
                if x == 1:
                    j = i
                else:
                    j = i + x  # The next x must be placed at i + x.

                if not isUsed[x - 1] and j < N and rslt[j] == 0:
                    isUsed[x - 1], rslt[i], rslt[j] = True, x, x
                    if dfs(i + 1):
                        return True

                    isUsed[x - 1], rslt[i], rslt[j] = False, 0, 0  # Rollback.

            return False

        N = (n << 1) - 1
        rslt = [0] * N
        isUsed = [False] * n
        dfs(0)
        return rslt


print(Solution().constructDistancedSequence(3))
