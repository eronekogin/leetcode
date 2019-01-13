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

        n = 0

        while x > n:  # Reverse only half digits of x to avoid overflow
            x, r = divmod(x, 10)
            n = n * 10 + r

        return x == n or x == n // 10  # even and odd case


print(Solution().isPalindrome(1110))
