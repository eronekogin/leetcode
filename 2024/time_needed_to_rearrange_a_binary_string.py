"""
https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/description/
"""


class Solution:
    """
    Solution
    """

    def seconds_to_remove_occurrences(self, s: str) -> int:
        """
        For any 1 at index i, if it has x leading zeros, it will take x seconds to
        move the current 1 to the left.

        If index i - 1 also contains 1, it will take x + 1 seconds to move the
        current 1 to the left.
        """
        seconds = leading_zeros = 0
        for c in s:
            if c == '0':
                leading_zeros += 1
                continue

            if leading_zeros > 0:
                seconds = max(seconds + 1, leading_zeros)

        return seconds


print(Solution().seconds_to_remove_occurrences('0110101'))
