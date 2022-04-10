"""
https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


class ProductOfNumbers:

    def __init__(self):
        self.prefixProducts = [1]

    def add(self, num: int) -> None:
        if not num:  # If current added num is zero.
            self.prefixProducts = [1]
        else:
            self.prefixProducts.append(self.prefixProducts[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefixProducts):  # Must have zero added before.
            return 0

        return self.prefixProducts[-1] // self.prefixProducts[-1 - k]
