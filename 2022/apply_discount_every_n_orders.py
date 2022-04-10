"""
https://leetcode.com/problems/apply-discount-every-n-orders/
"""


class Cashier:

    def __init__(
        self,
        n: int,
        discount: int,
        products: list[int],
        prices: list[int]
    ):
        self.n = n
        self.discount = discount
        self.menu = {
            product: price
            for product, price in zip(products, prices)
        }
        self.customerCnt = 0

    def getBill(
        self,
        products: list[int],
        amounts: list[int]
    ) -> float:
        totalBill = sum(
            self.menu[product] * amount
            for product, amount in zip(products, amounts)
        )

        self.customerCnt = (self.customerCnt + 1) % self.n
        if self.customerCnt == 0:
            return totalBill * (100 - self.discount) / 100

        return totalBill
