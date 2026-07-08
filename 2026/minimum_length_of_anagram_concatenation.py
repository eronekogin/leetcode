"""
https://leetcode.com/problems/minimum-length-of-anagram-concatenation/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def min_anagram_length(self, s: str) -> int:
        """
        min anagram length
        """
        def check(k: int) -> bool:
            cnt = Counter(s[:k])
            return all(
                Counter(s[i: i + k]) == cnt
                for i in range(k, n, k)
            )

        # find factors of n
        n = len(s)
        factors: set[int] = set()
        for d in range(1, int(n ** 0.5) + 1):
            q, r = divmod(n, d)
            if r > 0:
                continue

            factors.add(d)
            factors.add(q)

        for f in sorted(factors):
            if check(f):
                return f

        return -1


print(Solution().min_anagram_length('cdef'))
