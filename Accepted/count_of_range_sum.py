"""
https://leetcode.com/problems/count-of-range-sum/
"""


from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Count the sum of the first k numbers and store them in sums list.
        sums = [0]
        for num in nums:
            sums.append(sums[-1] + num)

        def sort_and_count(start: int, end: int) -> int:
            mid = start + ((end - start) >> 1)
            if start == mid:  # Not possible to be divided into two halfs.
                return 0

            rangeCnt = sort_and_count(start, mid) + sort_and_count(mid, end)
            low = high = mid
            for left in sums[start: mid]:
                while low < end and sums[low] - left < lower:
                    # Try to find the first index on the right half that has
                    # sums[low] - left >= lower.
                    low += 1

                while high < end and sums[high] - left <= upper:
                    # Try to find the first index on the left half that has
                    # sums[high] - left > higher.
                    high += 1

                # Now all the ranges between index high and low satisfied the
                # condition that sums[k] - left is between [lower, upper].
                rangeCnt += high - low

            # Use sort to keep the [start: end) sorted.
            sums[start: end] = sorted(sums[start: end])

            return rangeCnt

        return sort_and_count(0, len(sums))


print(Solution().countRangeSum([0, -1, 1, 2, -3, -3], -3, 1))
