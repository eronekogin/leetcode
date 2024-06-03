"""
https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
"""


class Solution:
    """
    Solution
    """

    def largest_good_integer(self, num: str) -> str:
        """
        largest good integer
        """
        max_num = ''
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                max_num = max(max_num, num[i: i + 3])

        return max_num
