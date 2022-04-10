"""
https://leetcode.com/problems/longest-turbulent-subarray/
"""


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        """
        1. The only thing that matters is the comparision result between
            adjancent numbers. When the rule is broken, we should calculate
            the current length of the subarray that follows the rule.
        2. Then we could use sliding window to handle that.
        """
        def cmp(x: int, y: int) -> bool:
            if x < y:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        N = len(arr)
        start, rslt = 0, 1
        for end in range(1, N):
            c = cmp(arr[end - 1], arr[end])
            if c == 0:
                start = end
            elif end == N - 1 or c * cmp(arr[end], arr[end + 1]) != -1:
                rslt = max(rslt, end - start + 1)
                start = end

        return rslt
