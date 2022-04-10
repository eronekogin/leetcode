"""
https://leetcode.com/problems/minimize-deviation-in-array/
"""


from heapq import heappush, heappop


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        """
        1. For each number in the given list, calculate the lower and the
            higher bound it could reach:
            1.1 For odd numbers, it is [x, x * 2].
            1.2 For even numbers, it is
                [keep divide by 2 until it becomes an odd number, x].

        2. Then store those bounds into a heap and set the initial difference
            to the maximum lower bound - the minimum lower bound.

        3. Then we keep looking at the smallest lower bound in the heap:
            3.1 If lower bound * 2 is still less than higher bound, we push
                [lower * 2, higher] to the heap.
            3.2 Else, we could add increase the smallest lower bound any more,
                thus the current difference is our answer.
        """
        def get_bound(i: int) -> tuple[int]:
            if i & 1:  # Even number:
                return (i, i << 1)
            else:  # Odd number.
                low = i
                while not low & 1:
                    low >>= 1

                return (low, i)

        maxVal = float('-inf')
        h = []
        for num in nums:
            low, high = get_bound(num)
            heappush(h, (low, high))
            maxVal = max(maxVal, low)

        minDiff = maxVal - h[0][0]
        while True:
            low, high = heappop(h)
            if low >= high:  # Could not increase lower bound any more.
                break

            low <<= 1
            maxVal = max(maxVal, low)
            heappush(h, (low, high))
            minDiff = min(minDiff, maxVal - h[0][0])

        return minDiff
