"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
"""


class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        """
        Keep counting the total sum, for the current total sum:
        1. If it is odd, any previous even odd sum could count as 1 result, as
            from the previous odd total sum to the current total sum, the
            subarray between them has odd sum.
        2. At the end we also need to add totalPreOddSums to the cnt, as that
            is the number of odd sums of subarrays starting with index 0.
        """
        totalPreEvenSums = totalPreOddSums = 0
        cnt = 0
        currSum = 0
        for num in arr:
            currSum += num
            if currSum & 1:
                cnt += totalPreEvenSums
                totalPreOddSums += 1
            else:
                cnt += totalPreOddSums
                totalPreEvenSums += 1

        return (totalPreOddSums + cnt) % (10 ** 9 + 7)


print(Solution().numOfSubarrays([1, 3, 5]))
