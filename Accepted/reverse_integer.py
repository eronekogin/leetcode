"""
https://leetcode.com/problems/reverse-integer/submissions/
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x

        # Assume running on 32 bits machine.
        MAXINT = ((1 << 31) - 1) // 10  # (2^31 - 1) // 10

        # % is different in python than c, convert to positive first.
        t = abs(x)
        rslt = 0

        while t != 0:
            t, r = divmod(t, 10)

            if rslt > MAXINT:
                return 0  # Overflow

            if (rslt == MAXINT) and ((x > 0 and r > 7) or (x < 0 and r > 8)):
                return 0  # Overflow

            rslt = rslt * 10 + r

        if x < 0:
            rslt *= -1

        return rslt


nums = [-123]
s = Solution()
for num in nums:
    print('{0}->{1}'.format(num, s.reverse(num)))
