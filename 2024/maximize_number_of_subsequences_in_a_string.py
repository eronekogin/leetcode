"""
https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_subsequence_count(self, text: str, pattern: str) -> int:
        """
        maximum_subsequence_count
        """
        leading_p0 = 0
        trailing_p1 = 0
        cnt = 0
        for c in text:
            # pattern 0 and pattern 1 can be the same char.
            if c == pattern[1]:
                trailing_p1 += 1
                cnt += leading_p0

            if c == pattern[0]:
                leading_p0 += 1

        return cnt + max(leading_p0, trailing_p1)


print(Solution().maximum_subsequence_count("abdcdbc", "ac"))
