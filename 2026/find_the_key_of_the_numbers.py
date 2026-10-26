"""
https://leetcode.com/problems/find-the-key-of-the-numbers/description/
"""


class Solution:
    """
    Solution
    """
    def generate_key(self, num1: int, num2: int, num3: int) -> int:
        """
        generate key
        """
        rslt = 0
        for i in range(3, 0, -1):
            q1, num1 = divmod(num1, 10 ** i)
            q2, num2 = divmod(num2, 10 ** i)
            q3, num3 = divmod(num3, 10 ** i)
            rslt = rslt * 10 + min(q1, q2, q3)

        return rslt * 10 + min(num1, num2, num3)
