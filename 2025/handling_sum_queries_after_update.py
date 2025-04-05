"""
https://leetcode.com/problems/handling-sum-queries-after-update/description/
"""


class Solution:
    """
    Solution
    """

    def handle_query(
        self,
        nums1: list[int],
        nums2: list[int],
        queries: list[list[int]]
    ) -> list[int]:
        """
        handle query
        """
        init = 1 << (len(nums1))

        n1 = 0
        for x in nums1:
            n1 = (n1 << 1) + x

        s2 = sum(nums2)
        rslt: list[int] = []

        for q in queries:
            if q[0] == 1:
                l = (init >> q[1]) - 1
                r = (init >> (q[2] + 1)) - 1
                n1 = n1 ^ l ^ r
            elif q[0] == 2:
                s2 += q[1] * (n1.bit_count())
            else:
                rslt.append(s2)

        return rslt


print(Solution().handle_query(
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
    [30, 46, 43, 34, 39, 16, 14, 41, 22, 11, 32, 2,
        44, 12, 22, 36, 44, 49, 50, 10, 33, 7, 42],
    [[1, 15, 21], [3, 0, 0], [3, 0, 0], [2, 21, 0], [2, 13, 0], [3, 0, 0]]
))
