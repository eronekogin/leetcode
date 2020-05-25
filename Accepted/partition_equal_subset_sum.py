"""
https://leetcode.com/problems/partition-equal-subset-sum/
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Take dp[i][j] as whether if we could pick some numbers from nums[:i]
        to form a summary of j. Then we have:

            dp[i+1][j] = dp[i][j]  # Do not pick nums[i+1]
        or (j >= nums[i + 1] and dp[i][j-nums[i+1]])  # Pick nums[i+1].

        Where dp[0][0] is 1 as we could always pick 0 numbers to form a
        summary of 0.

        Then dp[i + 1][*] only depends on the items in dp[i][*], we could
        reduce the 2d dp to a 1d dp, which we have:

            dp[j] = dp[j] or (j > nums[i + 1] and dp[j - nums[i + 1]])
        """
        if not nums or len(nums) < 2:
            return False

        t = sum(nums)
        if t & 1:  # Total summary is odd.
            return False

        t >>= 1  # Get half of the target.
        dp = [1] + [0] * t
        currSum = 0
        for num in nums:
            for i in reversed(range(num, min(currSum + num, t) + 1)):
                dp[i] = dp[i] or dp[i - num]

            if dp[t]:  # Found.
                return True

            currSum += num

        return dp[t] == 1


print(Solution().canPartition([23, 13, 11, 7, 6, 5, 5]))
