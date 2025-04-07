"""
https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/description/
"""


class Solution:
    """
    Solution
    """

    def min_operations(self, n: int) -> int:
        """
        min operations
        """
        digits: list[int] = []
        while n:
            digits.append(n & 1)
            n >>= 1

        digits.append(0)
        nd = len(digits)
        ops = 0

        start = end = 0
        while end < nd:
            if digits[end] == 1:
                start = end
                while end + 1 < nd and digits[end + 1] == 1:
                    end += 1

                ops += 1
                if end + 1 < nd and end - start + 1 > 1:
                    digits[end + 1] = 1

            end += 1

        return ops


print(Solution().min_operations(54))
