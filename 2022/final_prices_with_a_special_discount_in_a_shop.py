"""
https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
"""


class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack: list[int] = []
        finalPrices: list[int] = list(prices)
        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                finalPrices[stack.pop()] -= p

            stack.append(i)

        return finalPrices
