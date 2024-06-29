"""
https://leetcode.com/problems/apply-discount-to-prices/description/
"""


class Solution:
    """
    Solution
    """

    def discount_prices(self, sentence: str, discount: int) -> str:
        """
        discount prices
        """
        def apply_discount(w: str):
            if len(w) < 2 or not w.startswith('$'):
                return w

            if any(not c.isdigit() for c in w[1:]):
                return w

            price = int(w[1:])
            updated_price = price * (1 - discount / 100)
            return f'${updated_price:.2f}'

        return ' '.join(apply_discount(w) for w in sentence.split())
