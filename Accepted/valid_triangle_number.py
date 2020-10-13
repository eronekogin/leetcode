"""
https://leetcode.com/problems/valid-triangle-number/
"""


from typing import List
from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        Sort the list in ascending order so that for any triplets [a, b, c], 
        a <= b <= c, then we just need to check a + b > c and skip the other
        two checks c + b > a and c + a > b.
        """
        cnt, n = 0, len(nums)
        sortedNums = sorted(nums)
        for i in range(n - 2):
            if sortedNums[i]:
                k = i + 2
                for j in range(i + 1, n - 1):
                    k = bisect_left(
                        sortedNums, sortedNums[i] + sortedNums[j], k, n)
                    cnt += k - j - 1

        return cnt


print(Solution().triangleNumber([0, 1, 1, 1]))
