"""
https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/
"""


class Solution:
    """
    Solution
    """

    def count_digits(self, num: int) -> int:
        """
        count digits
        """
        cnt = 0
        x = num
        while x:
            x, d = divmod(x, 10)
            cnt += (num % d == 0)

        return cnt


print(Solution().count_digits(1248))
