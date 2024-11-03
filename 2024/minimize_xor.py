"""
https://leetcode.com/problems/minimize-xor/description/
"""


class Solution:
    """
    Solution
    """

    def minimize_xor(self, num1: int, num2: int) -> int:
        """
        minimize xor
        """
        a, b = num1.bit_count(), num2.bit_count()
        rslt = num1
        for i in range(32):
            if a > b and (1 << i) & num1 > 0:
                rslt ^= 1 << i
                a -= 1

            if a < b and (1 << i) & num1 == 0:
                rslt ^= 1 << i
                a += 1

            if a == b:
                return rslt

        return -1


print(Solution().minimize_xor(1, 12))
