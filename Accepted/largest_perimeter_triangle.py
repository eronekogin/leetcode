"""
https://leetcode.com/problems/largest-perimeter-triangle/
"""


class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        """
        1. Sort the nums in ascending order.
        2. Then for any group a <= b <= c, we only need to check if a + b > c
            to see if (a, b, c) could form a valid triangle.
        3. Then we scan from the right to left in order to find the maximum
            perimeter of the triangle:
            3.1 If the most adjancent group i, i + 1, i + 2 cannot form a 
                triangle, the remaining items less than i cannot form a
                triangle with i + 2 either.
                3.1.1 So if the above case happen, i + 2 should be skipped, 
                    then we should go ahead and choose i + 1 as our c.
            3.2 If the most adjancent group i, i + 1, i + 2 can form a
                triangle, it must have the largest perimeter. As if the
                remaining items less than i can form a triangle with i + 2,
                its perimeter must be less than the current triangle.  
        """
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 3, -1, -1):
            if sortedNums[i] + sortedNums[i + 1] > sortedNums[i + 2]:
                return sortedNums[i] + sortedNums[i + 1] + sortedNums[i + 2]

        return 0  # Not able to form any triangle.
