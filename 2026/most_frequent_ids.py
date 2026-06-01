"""
https://leetcode.com/problems/most-frequent-ids/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def most_frequent_ids(self, nums: list[int], freq: list[int]) -> list[int]:
        """
        most frequent ids
        """
        cnt: dict[int, int] = {}
        rslt: list[int] = []
        heap: list[tuple[int, int]] = []
        for x, f in zip(nums, freq):
            cnt[x] = max(0, cnt.get(x, 0) + f)
            heappush(heap, (-cnt[x], x))

            # handle lazy result
            while -heap[0][0] != cnt[heap[0][1]]:
                heappop(heap)

            rslt.append(-heap[0][0])

        return rslt
