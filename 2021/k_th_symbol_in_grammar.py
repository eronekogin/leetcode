"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
"""


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        """
        1. For each adjancent row, the second row's first half is the same as
            the first row and the second row's second half is the complement of
            the first half.
        2. If K is within the first half of the row, we go ahead and check
            where K is in the previous row.
        3. If K is within the second half of the row, we go ahead and check
            where K is in the previous row, but return its complement as the
            result.
        """
        if N == 1 and K == 1:
            return 0

        m = 1 << (N - 2)  # = 2^(N - 1) // 2.
        if K <= m:
            return self.kthGrammar(N - 1, K)
        else:
            return 1 - self.kthGrammar(N - 1, K - m)


print(Solution().kthGrammar(4, 5))
