"""
https://leetcode.com/problems/minimum-operations-to-collect-elements/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, nums: list[int], k: int) -> int:
        """
        min operations
        """
        collection = [False] * k
        actions = 0
        curr_sum = 0

        for x in reversed(nums):
            actions += 1
            if x > k or collection[x - 1]:
                continue

            collection[x - 1] = True
            curr_sum += 1

            if curr_sum == k:
                break

        return actions


print(Solution().min_operations([3, 1, 5, 4, 2], 2))
