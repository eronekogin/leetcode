"""
https://leetcode.com/problems/find-products-of-elements-of-big-array/description/
"""


from bisect import bisect_left


class Solution:
    """
    Solution
    """

    def find_products_of_elements(self, queries: list[list[int]]) -> list[int]:
        """
        find products of elements
        """
        def count(x):
            """
            find the total number of one bits from range [0, x - 1]
            """
            if x == 0:
                return 0

            # Find the largest power of 2 that is less than x
            b = x.bit_length() - 1
            v = 1 << b

            # For each column in the numbers from 0 to 2^b - 1,
            # it has half zeros and half ones, so we have
            # b * (v // 2) ones in the end
            res = b * (v >> 1)

            # For the remaining numbers 2^b to x - 1:
            # 1. Since the remaining numbers all set 1 in its leftmost bit,
            #    we have (x - 1 - v + 1) = x - v ones.
            # 2. Then we count the ones in the remaining columns, which is
            #    count(x - v)
            return res + count(x - v) + x - v

        def mul(x):
            """
            calculate the sum of total numbers from range [0, x - 1]
            """
            if x == 0:
                return 0

            # Find the largest power of 2 that is less than x
            b = x.bit_length() - 1
            v = 1 << b

            # Check [0, 2^b - 1] first:
            # The sum equals to 2^(b - 1) * (0 + 1 + ... + b - 1)
            # = 2^(b - 1) * b * (b - 1) // 2
            # = b * (b - 1) * 2 ^ b // 4
            res = ((b - 1) * b * v) >> 2

            # Check the remaining
            return res + mul(x - v) + b * (x - v)

        def query(k):
            if k == 0:
                return 0

            k += 1  # make it 1-indexed
            x = bisect_left(range(1, 10 ** 15), k, key=count)

            res = mul(x)

            k -= count(x)  # check how many numbers remaining

            for _ in range(k):
                b = x & -x  # Get the lowest set bit of x
                res += b.bit_length() - 1  # Convert it to its exponent of 2
                x -= b  # Subtract it from x

            return res

        return [pow(2, query(j) - query(i - 1), mod) for i, j, mod in queries]
