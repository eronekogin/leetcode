"""
https://leetcode.com/problems/super-pow/
"""


from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        """
        Facts:
            AB % k = ((A % k) * (B % k)) % k

        Suppose A = ak + c, B = bk + d, then:
        1. AB = abk^2 + adk + cbk + cd
        2. A % k = c, B % k = d
        So AB % k = cd % k = ((A % k) * (B % k)) % k.
        Then based on the above we could also have:
        (A ^ X) % k = ((A % k) ^ x) % k.

        Then we have:
        a^123 % k = 
            ((a^120 % k) * (a^3 % k)) % k =
            ((a^12)^10 % k) * (a^3 % k)) % k =
            (((a^12) % k) ^ 10) % k) * (a^3 % k)) % k

        Suppose f(a, b) = a^b % k, we have:
        a^123 % k = (f(f(a, 12), 10) * f(a, 3)) % k
        """
        if not b:
            return 1

        if len(b) == 1:
            return (a ** b[0]) % 1337

        return (self.superPow(self.superPow(a, b[:-1]), [10]) * self.superPow(
            a, b[-1:])) % 1337

    def superPow2(self, a: int, b: List[int]) -> int:
        """
        Use Euler's theorem: a^phi(n) = 1 % n, where a and n are coprime and
        phi(n) is the total number of primes that are less than n.

        Also, phi(n) = n - 1 if n is a prime.

        1337's factors are only 7 and 191. So
        phi(1337) = phi(7) * phi(191) = 6 * 190 = 1140.

        Then we have:
        1. If a and 1337 are coprime, then (a^1140) % 1337 = 1, so
        a^b = a^(1140q + r) = (a^1140)^q * a^r ->
        (a^b) % 1337 = (a^r) % 1337 = (a^(b % 1140)) % 1337.

        2. If a could be divded by 1337, the modular will be 0.

        3. If a contains factors like 7 or 191, suppose a = 7^n * x, where
        x and a are coprime and b = 1140q + r, then we have:
        a^b % 1337 = (7^n * x)^(1140q + r) % 1337 =
        (7^(1140nq + nr) % 1337 * x^(1140q + r) % 1337) % 1337

        Since x and 1137 are coprime, x^1140 % 1337 = 1, then we have:
        a^b % 1337 = (7^(1140nq + nr) % 1337 * x^r % 1337) % 1337 =
        (7*(7^(1140nq + nr - 1) % 191) * x^r % 1337) % 1337

        Since 7 and 191 are coprime, so 7^190 % 191 = 1 ->
        a^b % 1337 = (7*(7^(nr - 1) % 191) * x^r % 1337) % 1337 =
        (7^nr % 1337 * x ^ r % 1337) % 1337
        = (7^n * x) ^ r % 1337 = a^r % 1337 = (a^(b % 1140)) % 1337.


        4. We should avoid the case when b is divisible by 1140, which we
        simply add 1140 to the e to make sure of it.
        """
        if a % 1337 == 0:
            return 0

        e = 0
        for num in b:
            e = 10 * e + num

        # (a^b) % k = ((a % k)^b) % k.
        return ((a % 1337) ** (1140 + e % 1140)) % 1337
