"""
https://leetcode.com/problems/dice-roll-simulation/
"""


class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        faces = len(rollMax)

        # Dp[r][c] stands for the number of combinations at the rth roll with
        # sequence ending at face c.
        dp = [[0 for _ in range(faces + 1)] for _ in range(n + 1)]

        # Initialization.
        # Roll zero times, the total combination is 1.
        dp[0][faces] = 1

        # Roll one time, the total combination ends at c is 1.
        for c in range(faces):
            dp[1][c] = 1

        # Roll one time, the total combination of all is faces.
        dp[1][faces] = faces

        # Calculate the remaining combinations.
        for r in range(2, n + 1):
            for c in range(faces):
                dp[r][c] = dp[r - 1][faces]

                if r - 1 - rollMax[c] >= 0:
                    dp[r][c] -= dp[r - 1 - rollMax[c]][faces] - \
                        dp[r - 1 - rollMax[c]][c]

            dp[r][faces] = sum(dp[r])

        return dp[n][faces] % (10 ** 9 + 7)
