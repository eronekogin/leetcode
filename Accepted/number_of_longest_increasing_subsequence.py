"""
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""


from typing import List

from collections import defaultdict
from bisect import bisect_left


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """
        Follow the same dp solution to find the length of the longest
        increasing subsequence. And we also need to store the total number of
        sub sequences with the same length.
        """
        if not nums:
            return 0

        lis = [float('-inf')]
        memo = defaultdict(lambda: defaultdict(int))
        memo[0][float('-inf')] = 1
        for num in nums:
            lisLen = bisect_left(lis, num)
            if lisLen == len(lis):
                lis.append(num)
            else:
                lis[lisLen] = num

            memo[lisLen][num] += sum(
                v
                for k, v in memo[lisLen - 1].items()
                if k < num
            )

        # After processing the whole given list, the current length of lis is
        # the length of the longest increasing subsequence. So we just need to
        # sum its counts.
        return sum(memo[len(lis) - 1].values())


print(Solution().findNumberOfLIS([1, 3, 5, 4, 7]))
