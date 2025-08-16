"""
https://leetcode.com/problems/maximum-sum-queries/description/
"""


from bisect import bisect_left


class Solution:
    """
    Solution
    """

    def maximum_sum_queries(
        self,
        nums1: list[int],
        nums2: list[int],
        queries: list[list[int]]
    ) -> list[int]:
        """
        maximum sum queries
        """
        pairs = sorted(zip(nums1, nums2), reverse=True)
        sorted_queries = sorted(
            [(x, y, i) for i, (x, y) in enumerate(queries)],
            reverse=True
        )
        rslt = [0] * len(queries)
        max_y = 0
        sorted_y_to_sums: list[tuple[int, int]] = []

        ix = 0
        n = len(pairs)
        for x, y, iq in sorted_queries:
            while ix < n and pairs[ix][0] >= x:
                if pairs[ix][1] > max_y:
                    max_y = pairs[ix][1]
                    while (
                        sorted_y_to_sums and
                        sorted_y_to_sums[-1][1] < sum(pairs[ix])
                    ):
                        sorted_y_to_sums.pop()

                    sorted_y_to_sums.append((max_y, sum(pairs[ix])))

                ix += 1

            i = bisect_left(sorted_y_to_sums, (y, 0))
            rslt[iq] = (
                sorted_y_to_sums[i][1]
                if i < len(sorted_y_to_sums) else -1
            )

        return rslt
