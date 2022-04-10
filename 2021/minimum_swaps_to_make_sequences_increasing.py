"""
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
"""


class Solution:
    def minSwap(self, A: list[int], B: list[int]) -> int:
        """
        Suppose swapCnt[i] stands for the minimum swaps we need when 
        swapping the ith element in both list and fixCnt[i] stands for the 
        minimum swaps we need when not swapping the ith element in both list.
        Then we have:
            1. If A[i - 1] >= B[i] or B[i - 1] >= A[i], the swap for the ith
                element should be the same as the i-1th element. So we have:
                    swapCnt[i] = swapCnt[i - 1] + 1
                    fixCnt[i] = fixCnt[i - 1]
            2. If A[i - 1] >= A[i] or B[i - 1] >= B[i], the swap for the ith
                element should be the opposite of the i-1th element. So we
                have:
                    swapCnt[i] = fixCnt[i - 1] + 1
                    fixCnt[i] = swapCnt[i]
            3. For other cases, we could either swap the ith element or not,
                so we just take the minimum value from the previous step:
                    fixCnt[i] = min(swapCnt[i - 1], fixCnt[i - 1])
                    swapCnt[i] = fixCnt[i] + 1
        """
        swapCnt, fixCnt = 1, 0
        for i in range(1, len(A)):
            if A[i - 1] >= B[i] or B[i - 1] >= A[i]:
                swapCnt += 1
            elif A[i - 1] >= A[i] or B[i - 1] >= B[i]:
                swapCnt, fixCnt = fixCnt + 1, swapCnt
            else:
                fixCnt = min(swapCnt, fixCnt)
                swapCnt = fixCnt + 1

        return min(swapCnt, fixCnt)


print(Solution().minSwap(
    [1, 3, 5, 4],
    [1, 2, 3, 7]
))
