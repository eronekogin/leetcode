"""
https://leetcode.com/problems/split-with-minimum-sum/description/
"""


class Solution:
    """
    Solution
    """

    def split_num(self, num: int) -> int:
        """
        split num
        """
        digits: list[int] = []
        while num:
            num, r = divmod(num, 10)
            digits.append(r)

        digits.sort()
        n1 = n2 = 0
        for i in range(0, len(digits), 2):
            n1 = n1 * 10 + digits[i]

            if i + 1 < len(digits):
                n2 = n2 * 10 + digits[i + 1]

        return n1 + n2
