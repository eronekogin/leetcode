"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Cheat: return sorted(nums, reverse=True)[k - 1]

        Python's sort function uses timsort, which is an optimized
        merge sort + quick sort.

        Here we implement quick sort as the solution for this question.
        """
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

        start, end, target = 0, len(nums) - 1, k - 1
        while True:
            pivot = get_pivot(start, end)
            if target > pivot:
                start = pivot + 1
            elif target < pivot:
                end = pivot - 1
            else:
                return nums[pivot]


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(Solution().findKthLargest(nums, 4))
