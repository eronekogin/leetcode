"""
https://leetcode.com/problems/find-the-distinct-difference-array/description/
"""


class Solution:
    """
    Solution
    """

    def distinct_difference_array(self, nums: list[int]) -> list[int]:
        """
        distinct difference array
        """
        n = len(nums)
        diffs = [0] * n
        prefix = {}
        suffix = set()

        for x in nums:
            prefix[x] = prefix.get(x, 0) + 1

        for i in range(n - 1, -1, -1):
            x = nums[i]
            diffs[i] = len(prefix) - len(suffix)
            suffix.add(x)
            prefix[x] -= 1
            if prefix[x] == 0:
                del prefix[x]

        return diffs
