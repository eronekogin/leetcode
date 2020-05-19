"""
https://leetcode.com/problems/split-array-largest-sum/
"""


from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        """
        The total cut is in [1, len(nums)], which means the range of the
        largest summary of sub arrays is from [max(nums), sum(nums)], given
        that all the numbers in nums are non-negative.

        Then we could perform binary search in this sum range to find the
        smallest one.
        """
        minSum = maxSum = 0
        for num in nums:
            minSum = max(minSum, num)
            maxSum += num

        if m == 1:
            return maxSum

        if m == len(nums):
            return minSum

        while minSum < maxSum:
            midSum = minSum + ((maxSum - minSum) >> 1)

            # Check if midSum could be formed by nums with m cut.
            cut, subSum = 1, 0
            for num in nums:
                if subSum + num <= midSum:
                    subSum += num
                else:
                    subSum = num
                    cut += 1
                    if cut > m:
                        break

            if cut <= m:  # midSum is possible, try to find smaller midSum.
                maxSum = midSum
            else:  # Has to find larger midSum.
                minSum = midSum + 1

        return minSum


print(Solution().splitArray([7, 2, 5, 8, 3], 2))
