"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
"""


from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def divide(i: int) -> bool:
            if i < 0:  # Have placed all the candidates into the subsets.
                return True

            for j in range(requiredSets):
                subSums[j] += candidates[i]
                if subSums[j] <= subSum and divide(i - 1):
                    return True

                subSums[j] -= candidates[i]
                if subSums[j] == 0:
                    # No need to put the same number into other empty subsets.
                    break

            return False

        subSum, r = divmod(sum(nums), k)
        if r:  # Could not be divided equally.
            return False

        candidates, requiredSets = [], k
        for num in nums:
            if num > subSum:  # Cannot fit in any subset.
                return False
            elif num == subSum:  # Single number fit into one subset.
                requiredSets -= 1
            else:
                candidates.append(num)

        subSums = [0] * requiredSets
        candidates.sort()
        return divide(len(candidates) - 1)


print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
