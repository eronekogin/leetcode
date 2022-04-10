"""
https://leetcode.com/problems/integer-to-english-words/
"""


from typing import List


class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Assumption: the input number <= 1000 ** 4.
        """
        to19 = [
            None,
            'One', 'Two', 'Three', 'Four',
            'Five', 'Six', 'Seven', 'Eight',
            'Nine', 'Ten', 'Eleven', 'Twelve',
            'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen',
            'Seventeen', 'Eighteen', 'Nineteen'
        ]
        tens = [
            None, None,
            'Twenty', 'Thirty', 'Forty', 'Fifty',
            'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        thousands = ['Thousand', 'Million', 'Billion']

        def words(n: int) -> List[str]:
            if not n:
                return []

            if n < 20:
                return [to19[n]]

            if n < 100:
                return [tens[n // 10]] + words(n % 10)

            if n < 1000:
                return [to19[n // 100]] + ['Hundred'] + words(n % 100)

            # Check if less than 1 million, or less than 1 billion,
            # or less than 1 trillion.
            for i, s in enumerate(thousands, start=1):
                k = 1000 ** i
                if n < 1000 * k:
                    return words(n // k) + [s] + words(n % k)

        return ' '.join(words(num)) or 'Zero'


print(Solution().numberToWords(123))
