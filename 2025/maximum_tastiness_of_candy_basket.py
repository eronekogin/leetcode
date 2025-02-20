"""
https://leetcode.com/problems/maximum-tastiness-of-candy-basket/description/
"""


class Solution:
    """
    Solution
    """

    def maximum_tastiness(self, price: list[int], k: int) -> int:
        """
        maximum tastiness
        """
        def verify(x: int):
            prev = price[0]
            cnt = 1
            i = 1
            while cnt < k and i < len(price):
                if price[i] >= prev + x:
                    prev = price[i]
                    cnt += 1

                i += 1

            return cnt == k

        price.sort()
        l, r = 0, 10 ** 9
        while l < r:
            m = l + ((r - l) >> 1)
            if verify(m):
                l = m + 1
            else:
                r = m

        return l - 1


print(Solution().maximum_tastiness([13, 5, 1, 8, 21, 2], 3))
