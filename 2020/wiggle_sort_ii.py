"""
https://leetcode.com/problems/wiggle-sort-ii/
"""


from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]):
        if not nums:
            return

        n = len(nums)
        if n == 1:  # Only 1 element.
            return

        def get_pivot(start: int, end: int) -> int:
            """
            Select the middle item as the pivot value. Then put all the 
            items that are greater or equal than the pivot value to the left
            side of the pivot. Then return the pivot position.
            """
            selectedIdx = (start + end) // 2
            nums[selectedIdx], nums[end] = nums[end], nums[selectedIdx]
            pivot, pivotValue = start, nums[end]
            for i in range(start, end):
                if nums[i] >= pivotValue:
                    nums[pivot], nums[i] = nums[i], nums[pivot]
                    pivot += 1

            nums[pivot], nums[end] = nums[end], nums[pivot]
            return pivot

        def get_map_idx(origIdx: int) -> int:
            """
            Now we want all the numbers before median to be in the odd indexes
            of the result list and all the numbers after median to be in the
            even indexes of the result list. So that the result list will be
            wiggled. n | 1 will give us the next odd number if n is even, else
            same as n.

            Then (2i + 1) % (n | 1) will map the first half indexes to odd 
            ones while the remaining half indexes to even ones. 

            For example:
            0 1 2 3 4 5 -> 1 3 5 0 2 4.
            """
            return ((origIdx << 1) + 1) % (n | 1)

        # Try to find the median of the input list first.
        s, e, t = 0, n - 1, (n >> 1) - 1
        while True:
            p = get_pivot(s, e)
            if t > p:
                s = p + 1
            elif t < p:
                e = p - 1
            else:
                break

        median = nums[p]
        odd, even = 0, n - 1
        i = 0
        while i <= even:
            mi = get_map_idx(i)
            if nums[mi] > median:  # Should be placed to where odd is.
                mo = get_map_idx(odd)
                nums[mi], nums[mo] = nums[mo], nums[mi]
                i += 1
                odd += 1
            elif nums[mi] < median:  # Should be placed to where even is.
                me = get_map_idx(even)
                nums[mi], nums[me] = nums[me], nums[mi]
                even -= 1
            else:  # Same as median, no need to move.
                i += 1


print(Solution().wiggleSort([3, 1]))
