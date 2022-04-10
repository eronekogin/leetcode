"""
https://leetcode.com/problems/2-keys-keyboard/
"""


from typing import Iterator


class Solution:
    def minSteps(self, n: int) -> int:
        def do(currSteps: int, currChars: int, copiedChars: int) -> int:
            if currChars > n:  # Exceed.
                return float('inf')

            if currChars == n:  # Done.
                return currSteps

            if (currChars, copiedChars) not in memo:
                # Either copy all and paste or paste only.
                memo[(currChars, copiedChars)] = min(
                    do(currSteps + 2, currChars << 1, currChars),
                    do(currSteps + 1, currChars + copiedChars, copiedChars))

            return memo[(currChars, copiedChars)]

        if n == 1:
            return 0

        if n == 2:
            return 2

        memo = {}  # {(currChars, copiedChars): minSteps}.

        return do(2, 2, 1)

    def minSteps2(self, n: int) -> int:
        """
        Eventually all the operations will be divided into a few groups with
        one copy at the front following by a few paste actions as follows:
            CP CPP CPPP

        Suppose each group's length is L1, L2, ..., Ln, then our answer will be
        L1 + L2 + ... + Ln.

        1. Suppose Li is a composite number and suppose Li = p * q, then we
            could always split the Li group into two groups having p - 1 pastes
            and q - 1 pastes. Then the total steps of two groups will be p + q
            instead of pq.
        2. For any p > 1 and q > 1, p + q < pq, which means we get a smaller 
            results than the original grouping.

        Then in the end this problem becomes to find all the prime factors of
        n and sum them up.
        """
        def get_prime_factor(num: int) -> Iterator[int]:
            p, currNum = 2, num
            while p * p <= currNum:
                while not currNum % p:
                    currNum //= p
                    yield p

                p += 1

            if currNum > 1:  # The final factor.
                yield currNum

        return sum(get_prime_factor(n))

    def minSteps3(self, n: int) -> int:
        """
        Same idea as the second solution but could be more easily transferred
        to other languages.
        """
        p, rslt, currNum = 2, 0, n
        while p * p <= currNum:
            while not currNum % p:
                rslt += p
                currNum //= p

            p += 1

        if currNum == 1:
            currNum = 0

        return rslt + currNum


print(Solution().minSteps(3))
