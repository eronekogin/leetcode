"""
https://leetcode.com/problems/palindrome-number/
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        t, n = x, 0

        while t > n:  # Reverse only half digits of x to avoid overflow
            t, r = divmod(t, 10)
            n = n * 10 + r

        return t == n or t == n // 10  # even and odd case


print(Solution().isPalindrome(1110))
