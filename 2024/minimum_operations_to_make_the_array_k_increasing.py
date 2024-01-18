"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/description/
"""


from bisect import bisect_right


class Solution:
    """
    Solution
    """

    def k_increasing(self, arr: list[int], k: int) -> int:
        """
        k_increasing
        """
        def find_longest_increasing_subseqence(arr: list[int]):
            lis: list[int] = []
            for x in arr:
                if not lis or lis[-1] <= x:
                    lis.append(x)
                else:
                    j = bisect_right(lis, x)
                    lis[j] = x

            return len(lis)

        n = len(arr)
        rslt = 0
        for i in range(k):  # Divide original array into k separated arrays.
            subarray = arr[i: n: k]
            rslt += (
                len(subarray) -
                find_longest_increasing_subseqence(subarray)
            )

        return rslt
