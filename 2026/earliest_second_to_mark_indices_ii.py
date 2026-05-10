"""
https://leetcode.com/problems/earliest-second-to-mark-indices-ii/description/
"""


from heapq import heappop, heappush


class Solution:
    """
    Solution
    """

    def earliest_second_to_mark_indices(self, nums: list[int], change_indices: list[int]) -> int:
        """
        For each first occurrence of value at index i in change_indices, we can set nums[i - 1]
        to zero, which can be the most efficient way to reduce nums[i - 1].
        """
        def check(b: int) -> bool:
            heap = []
            capacity = 0

            for i in range(b - 1, -1, -1):
                if i in first_nums:
                    # We are using the current second to set the number to zero.
                    heappush(heap, nums[first_nums[i] - 1])

                    if capacity > 0:
                        # And if we still have capacity, we can use another second
                        # to mark it.
                        capacity -= 1
                    else:
                        # Taking the current second as more capacity.
                        capacity += 1

                        # We are trading the smallest number from heap with
                        # the current number so that the reduce and mark time
                        # for the smallest number is less than the current
                        # number. in this case, the current number is still
                        # set to zero and marked, no further capacity change.
                        heappop(heap)
                else:
                    capacity += 1

            # heap contains all the numbers that can be set to zero, so
            # in order to reduce the remaining numbers to zero, we have
            # to decrease them one by one, so the required seconds are
            # total - sum(heap).
            # Then we also need 1 second to mark each remaining number
            # which takes n - len(heap) seconds.
            # Then we check if the total required seconds <= capacity
            return total - sum(heap) + n - len(heap) <= capacity

        first_indices = {}
        for i, x in enumerate(change_indices):
            if nums[x - 1] and x not in first_indices:
                first_indices[x] = i

        first_nums = {i: x for x, i in first_indices.items()}
        n = len(nums)
        total = sum(nums)

        l, r = 0, len(change_indices) + 1
        while l < r:
            m = l + ((r - l) >> 1)
            if not check(m):
                l = m + 1
            else:
                r = m

        if l <= len(change_indices):
            return l

        return -1
