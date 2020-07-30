"""
https://leetcode.com/problems/target-sum/
"""


from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        Count the current summary level by level.
        """
        currSums = {0: 1}  # {currSum: total ways}
        for num in nums:
            nextSums = {}
            for currSum, cnt in currSums.items():
                nextSums[currSum + num] = nextSums.get(currSum + num, 0) + cnt
                nextSums[currSum - num] = nextSums.get(currSum - num, 0) + cnt

            currSums = nextSums

        return currSums.get(S, 0)


print(Solution().findTargetSumWays([1, 0], 1))
