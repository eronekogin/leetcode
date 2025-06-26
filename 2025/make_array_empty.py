"""
https://leetcode.com/problems/make-array-empty/description/
"""


class Solution:
    """
    Solution
    """

    def count_operations_to_empty_array(self, nums: list[int]) -> int:
        """
        In the first pass, no matter what is deleted or moved to the back, it
        takes n operations

        Then in the second pass, if we have removed i numbers previously, it 
        takes n - i operations for this pass.

        We do this until the array is empty.

        We should start a new pass when the nums is sorted and the current number's
        original index is less than the previous number's original index.
        """
        memo = {x: i for i, x in enumerate(nums)}
        operations = n = len(nums)

        nums.sort()
        for i in range(1, n):
            if memo[nums[i]] < memo[nums[i - 1]]:
                operations += n - i

        return operations


print(Solution().count_operations_to_empty_array([-4, -13, -12]))
