"""
https://leetcode.com/problems/smallest-good-base/
"""


from math import log2


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        """
        1. When a base is a good base, all the digits in the converted number
            is 1, which means 1 + k + k^2 + ... + k^m = n, so n > k^m.
        2. According to binomial theorem, (k + 1)^m = sum(c(m, i) * k^i), here
            c(m, i) means to choose i numbers of k from m, which is guranted to
            be greater or equal than 1, so (k + 1)^m > n.
        3. From 1 and 2 we could find that k has to be int(n^(1/m)).
        4. From proportion formular we have n = (1 - k^(m + 1)) // (1 - k),
            we could then use it to check if the target k and m pair is what
            we are looking for.
        5. The question assumes that the smallest base is 2, so the maximum
            number of items is when the base is 2, which is log(2, n).
        """
        totalSum = int(n)
        maxNumberOfItems = int(log2(totalSum))
        for m in range(maxNumberOfItems, 1, -1):  # [maxNumberOfItems, 2]
            k = int(totalSum ** (1 / m))  # Estimate proportion.

            # Calculate total sum.
            if (k ** (m + 1) - 1) // (k - 1) == totalSum:
                return str(k)

        return str(totalSum - 1)  # Not found from the above.
