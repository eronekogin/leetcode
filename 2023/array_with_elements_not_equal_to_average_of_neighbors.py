"""
https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
"""


class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        """
        Sort the array and then swap each neighbor with small, big, small, big pattern so that the middle number
        will never become the average of its neighbors as all the numbers in the original list is unique.
        """
        sortedNums = sorted(nums)
        for i in range(1, len(nums), 2):
            sortedNums[i], sortedNums[i - 1] = sortedNums[i - 1], sortedNums[i]

        return sortedNums 
        

print(Solution().rearrangeArray([1,5,2,6,3,7,4,8]))