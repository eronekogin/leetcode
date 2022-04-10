"""
https://leetcode.com/problems/counting-bits/
"""


from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        maxLen = num + 1
        rslt = [0] * maxLen
        for i in range(maxLen):
            if i & 1:  # i is an odd number.
                rslt[i] = rslt[i - 1] + 1  # i has one more 1 than i - 1.
            else:  # i is an even number.
                rslt[i] = rslt[i >> 1]  # i has same 1s as i >> 1.

        return rslt


print(Solution().countBits(25))
