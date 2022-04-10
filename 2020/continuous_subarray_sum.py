"""
https://leetcode.com/problems/continuous-subarray-sum/
"""


from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        The basic idea is for any summary s1 and s2, suppose s1 = ak + r1 and
        s2 = bk + r2. If r1 == r2, then s2 - s1 = (b - a)k which will be a
        multiple of k. So we keep adding each number to the total sum, and
        record the first time each sub sum occurs, then check if in the future
        there is a sub sum with the same remainder as the previous one. Then
        check if the sub array formed between those 2 sums contains more than
        1 item.
        """
        memo = {0: -1}  # {summary: the index where the summary first occurs}
        currSum = 0
        for i, n in enumerate(nums):
            currSum += n
            chkSum = currSum % k if k != 0 else currSum
            if chkSum in memo:
                # The subarray must contain at least 2 items.
                if i - memo[chkSum] > 1:
                    return True
            else:
                memo[chkSum] = i  # Record the index of the first occurrence.

        return False  # No solution at this stage.


print(Solution().checkSubarraySum([5, 0, 0], 0))
