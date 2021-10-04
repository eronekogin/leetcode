"""
https://leetcode.com/problems/last-stone-weight-ii/
"""


class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        """
        The problem is the same as to divide the stones into two groups so
        that the difference between those two groups is minimum.
        """
        sumMemo = {0}
        total = sum(stones)

        # Calculate unique sums of the divided groups.
        for stone in stones:
            sumMemo |= {stone + currSum for currSum in sumMemo}

        # Calculate the difference between any two groups.
        return min(abs((total - currSum) - currSum) for currSum in sumMemo)


print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))
