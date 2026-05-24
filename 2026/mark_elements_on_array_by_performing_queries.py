"""
https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/description/
"""


from heapq import heapify, heappop


class Solution:
    """
    Solution
    """

    def unmarked_sum_array(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        """
        unmarked sum array
        """
        heap = [(x, i) for i, x in enumerate(nums)]
        heapify(heap)
        rslt = [0] * len(queries)
        marked = set()
        total = sum(nums)
        for j, (i, k) in enumerate(queries):
            if i not in marked:
                marked.add(i)
                total -= nums[i]

            while heap and k:
                x, i2 = heappop(heap)
                if i2 not in marked:
                    total -= x
                    k -= 1
                    marked.add(i2)

            if not heap:
                break

            rslt[j] = total

        return rslt


print(Solution().unmarked_sum_array(
    [1, 2, 2, 1, 2, 3, 1], [[1, 2], [3, 3], [4, 2]]))
