"""
https://leetcode.com/problems/beautiful-arrangement-ii/
"""


from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        """
        1. When k = n - 1, then a possible construction of the target array
            could be [1, n, 2, n - 1, 3, n - 2, ...], which has n - 1 unique
            difference between adjancent items like [n - 1, n - 2, ..., 2, 1].
        2. So we first list [1, 2, ... , n - k - 1] which has only 1 unique
            difference. Then for the remainig k + 1 numbers from n - k to n,
            we could form the remaining list as Point 1 which gives us k unique
            difference like [k, k - 1, ..., 2, 1].
        3. Since the difference for the previous list is 1, we will finally
            have exactly k unique difference in the generated list.
        """
        rslt = list(range(1, n - k))
        left, right = n - k, n
        for i in range(k + 1):
            if i & 1:
                rslt.append(right - (i >> 1))
            else:
                rslt.append(left + (i >> 1))

        return rslt
