"""
https://leetcode.com/problems/pizza-with-3n-slices/
"""


class Solution:
    def maxSizeSlices(self, slices: list[int]) -> int:
        """
        1. This problem equals to find n numbers from a 3n length list whose
            sum is maximum. Meanwhile those picked n numbers should not be
            adjancent.
        2. At the same time since slices form a cycle, which means slices[0]
            and slices[-1] should not be picked at the same time.
        """
        def get_max_sum(numbers: list[int], totalPick: int) -> int:
            """
            Calculate the maximum sum by picking totalPick numbers out of 
            the input linear list.
            """
            N = len(numbers)
            dp = [[0] * (totalPick + 1) for _ in range(N + 1)]
            for totalLen in range(1, N + 1):
                for currPick in range(1, totalPick + 1):
                    if totalLen == 1:  # List only has one number.
                        dp[totalLen][currPick] = numbers[0]
                    else:
                        dp[totalLen][currPick] = max(
                            dp[totalLen - 1][currPick],
                            dp[totalLen - 2][currPick - 1] +
                            numbers[totalLen - 1]
                        )

            return dp[-1][-1]

        N = len(slices) // 3
        return max(
            get_max_sum(slices[0: len(slices) - 1], N),
            get_max_sum(slices[1:], N)
        )
