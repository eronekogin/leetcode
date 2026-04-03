"""
https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/description/
"""


from math import log


class Solution:
    """
    See https://leetcode.com/problems/maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k/solutions/4564468/python-binary-search-with-explaination-b-76lm/
    for more details
    """

    def find_maximum_number(self, k: int, x: int) -> int:
        """
        find maximum number
        """
        def get_price_sum(y: int) -> int:
            left_most = int(log(y, 2) + 1)
            y += 1
            rslt = 0

            for i in range(x, left_most + 1, x):
                block_size = 1 << i
                full_blocks = y // block_size

                full_block_ones = full_blocks * (block_size >> 1)
                remain_ones = max(
                    0,
                    (y % block_size) - (block_size >> 1)
                )

                rslt += full_block_ones + remain_ones

            return rslt

        l, r = 1, 10 ** 15
        while l <= r:
            m = l + ((r - l) >> 1)
            p = get_price_sum(m)
            if p <= k:
                l = m + 1
            else:
                r = m - 1

        return l - 1


print(Solution().find_maximum_number(9, 1))
