"""
https://leetcode.com/problems/gray-code/
"""

from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        rslt = [0]
        for i in range(n):
            # Gray code requires two successive elements should only
            # have 1 bit difference. So reverse the current rslt list
            # during each round of the loop.
            rslt += [(1 << i) + x for x in reversed(rslt)]

        return rslt


print(Solution().grayCode(2))
