"""
https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
"""


class Solution:
    """
    Solution
    """

    def sum_of_encrypted_int(self, nums: list[int]) -> int:
        """
        sum of encrypted int
        """
        def transform(x: int) -> int:
            """
            form the 111..111 with the same length as
            x, then the result would be max_d * rslt.

            for example, 543 becomes 111 * 5 = 555
            """
            rslt = 0
            max_digit = 0
            while x:
                x, r = divmod(x, 10)
                max_digit = max(max_digit, r)
                rslt = rslt * 10 + 1

            return max_digit * rslt

        return sum(
            map(transform, nums)
        )
