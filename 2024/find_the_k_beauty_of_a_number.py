"""
https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/
"""


class Solution:
    """
    Solution
    """

    def divisor_substrings(self, num: int, k: int) -> int:
        """
        divisor substrings
        """
        cnt = 0
        s = str(num)
        for i in range(len(s) - k + 1):
            x = int(s[i: i + k])
            cnt += (x > 0 and num % x == 0)

        return cnt


print(Solution().divisor_substrings(240, 2))
