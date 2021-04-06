"""
https://leetcode.com/problems/minimum-operations-to-make-array-equal/
"""


class Solution:
    def minOperations(self, n: int) -> int:
        """
        1. The total sum of the original array S = (1 + 2(n - 1) + 1) * n / 2
            = n * n.
        2. Since each operation won't change the total sum of the array, when
            all the numbers are equal in the final array, each number should
            be n * n / n = n.
        3. For minimum operation, we apply one operation on the current start
            and end element in the array, For example, the (first, last) pair
            will take n - 1 operations, and the (first + 1, last - 1) pair will
            take n - 3 operations, etc.
        4. So the total operations = (n - 1) + (n - 3) + ... + 1 = 
            (n - 1 + 1) * ((n - 1 - 1) / 2 + 1) / 2 = n * n / 4.
        """
        return n * n // 4
