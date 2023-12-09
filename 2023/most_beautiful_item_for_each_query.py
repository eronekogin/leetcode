"""
https://leetcode.com/problems/most-beautiful-item-for-each-query/
"""


from bisect import bisect_right


class Solution:
    """
    Solution
    """

    def maximum_beauty(self, items: list[list[int]], queries: list[int]) -> list[int]:
        """
        maximum_beauty
        """
        sorted_items = sorted(items)
        min_price, max_beauty = sorted_items[0]

        # generate left most list.
        for i, (_, curr_beauty) in enumerate(sorted_items):
            if curr_beauty > max_beauty:
                max_beauty = sorted_items[i][1]
            else:
                sorted_items[i][1] = max_beauty

        n = len(queries)
        rslt = [0] * n

        for i, p in enumerate(queries):
            if p >= min_price:
                x = bisect_right(sorted_items, [p, float('inf')])
                rslt[i] = sorted_items[x - 1][1]

        return rslt


print(Solution().maximum_beauty(
    [[1, 2], [3, 2], [2, 4], [5, 6], [3, 5]], [1, 2, 3, 4, 5, 6]))
