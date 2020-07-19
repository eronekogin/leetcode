"""
https://leetcode.com/problems/largest-palindrome-product/
"""


class Solution:
    def largestPalindrome1(self, n: int) -> int:
        if n == 1:
            return 9  # 3 * 3.

        maxNum = 10 ** n - 1
        minNum = maxNum // 10
        for high in range(maxNum, minNum, -1):
            # Construct the current palindrome based on the higher half.
            p = low = high
            while low:
                low, remain = divmod(low, 10)
                p = p * 10 + remain

            # Check if p could be divided by two n digits number.
            for i in range(maxNum, minNum, -1):
                q, r = divmod(p, i)
                if q > i:  # The remaining values are checked before.
                    break

                if not r:
                    return p % 1337

    def largestPalindrome2(self, n: int) -> int:
        """
        Math Solution:

        Suppose p = (10^n - i) * (10^n - j) = high * 10^n + low, then we have:
        p = 10^2n - (i + j) * 10^n + i * j = (10^n - i - j) * 10^n + i * j
        -> high = 10^n - i - j, low = i * j

        Suppose a = i + j, then we have:
        high = 10^n - a, low = i * (a - i)
        -> low + i^2 - a * i = 0
        -> low + (i - a/2)^2 - (a/2)^2 = 0
        -> (2i - a)^2 = a^2 - 4 * low

        Since both i and j are integers, 2i - a = 2i - i - j = i - j must be an
        integer, which means sqrt(a^2 - 4 * low) must be an integer.

        Besides, when p is a palindrome, the low could be calculated through
        high as it is a mirror of high.
        """
        if n == 1:
            return 9  # 3 * 3

        maxNum = 10 ** n
        maxMod = maxNum % 1337
        for a in range(2, maxNum):  # i >= 1, j >= 1, so a = i + j >= 2.
            low, high = 0, maxNum - a
            while high:  # Calculate lower half based on the higher half.
                high, r = divmod(high, 10)
                low = low * 10 + r

            x, y = a ** 2, low << 2
            if x > y:
                t = (x - y) ** 0.5
                if t == int(t):
                    # (high * maxNum + low) % 1337
                    return ((((maxNum - a) % 1337) * maxMod) % 1337 + low % 1337) % 1337
