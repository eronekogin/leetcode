"""
https://leetcode.com/problems/split-the-array/description/
"""


class Solution:
    """
    Solution
    """

    def is_possible_to_split(self, nums: list[int]) -> bool:
        """
        is possible to split
        """
        memo = {}
        for x in nums:
            curr = memo.get(x, 0)
            if curr == 2:
                return False

            memo[x] = curr + 1

        return True
