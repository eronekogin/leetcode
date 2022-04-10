"""
https://leetcode.com/problems/beautiful-array/
"""


class Solution:
    def beautifulArray(self, n: int) -> list[int]:
        """
        1. Suppose A is a beautiful array, then B = xA + y is still a
            beautiful array.
        2. Then we combine our B as follows:
            B = 2A - 1 + 2A
        3. The reason we conduct B like the above is because for x, y in
            2A - 1, 2A, x + y must be an odd number, so any such pair [x, y]
            will still be a beautiful array.
        """
        rslt = [1]
        while len(rslt) < n:
            rslt = [(i << 1) - 1 for i in rslt] + [i << 1 for i in rslt]

        return [i for i in rslt if i <= n]
