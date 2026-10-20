"""
https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/description/
"""


class Solution:
    """
    Solution
    """

    def largest_palindrome(self, n: int, k: int) -> str:
        """
        largest palindrome
        """
        if k == 1:
            return '9' * n

        if k == 2:
            if n <= 2:
                return '8' * n

            return '8' + '9' * (n - 2) + '8'

        if k == 3 or k == 9:
            return '9' * n

        if k == 4:
            if n <= 4:
                return '8' * n

            return '88' + '9' * (n - 4) + '88'

        if k == 5:
            if n <= 2:
                return '5' * n

            return '5' + '9' * (n - 2) + '5'

        if k == 6:
            if n <= 2:
                return '6' * n

            if n % 2 == 1:
                l = n // 2 - 1
                return '8' + '9' * l + '8' + '9' * l + '8'

            l = n // 2 - 2
            return '8' + '9' * l + '77' + '9' * l + '8'

        if k == 8:
            if n <= 6:
                return '8' * n

            return '888' + '9' * (n - 6) + '888'

        dic = {
            0: '',
            1: '7',
            2: '77',
            3: '959',
            4: '9779',
            5: '99799',
            6: '999999',
            7: '9994999',
            8: '99944999',
            9: '999969999',
            10: '9999449999',
            11: '99999499999'
        }

        l, r = divmod(n, 12)
        return '999999' * l + dic[r] + '999999' * l
