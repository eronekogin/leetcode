"""
https://leetcode.com/problems/number-of-distinct-roll-sequences/description/
"""


from collections import Counter
from math import gcd


class Solution:
    """
    Solution
    """

    def distinct_sequences(self, n: int) -> int:
        """
        distinct sequences
        """
        m = 10 ** 9 + 7
        curr_dp = {(7, 7): 1}
        candidates = {
            i: [j for j in range(1, 7) if gcd(i, j) == 1 and j != i]
            for i in range(1, 8)
        }

        for _ in range(n):
            next_dp = Counter()
            for a, b in curr_dp:
                for c in candidates[b]:
                    if a != c:
                        next_dp[b, c] = (next_dp[b, c] + curr_dp[a, b]) % m

            curr_dp = next_dp

        return sum(curr_dp.values()) % m


print(Solution().distinct_sequences(4))
