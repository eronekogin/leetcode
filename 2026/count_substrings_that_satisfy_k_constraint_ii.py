"""
https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/description/
"""


from itertools import accumulate


class Solution:
    """
    Solution
    """

    def count_k_constraint_substrings(self, s: str, k: int, queries: list[list[int]]) -> list[int]:
        """
        count k constraint substrings
        """
        n = len(s)
        max_rights = [0] * n
        min_lefts = [0] * n

        start = 0
        cnt = {'0': 0, '1': 0}
        for end, c in enumerate(s):
            cnt[c] += 1

            while cnt['0'] > k and cnt['1'] > k:
                cnt[s[start]] -= 1
                start += 1

            min_lefts[end] = start

        end = n - 1
        cnt = {'0': 0, '1': 0}
        for start in range(n - 1, -1, -1):
            cnt[s[start]] += 1

            while cnt['0'] > k and cnt['1'] > k:
                cnt[s[end]] -= 1
                end -= 1

            max_rights[start] = end

        pre_sums = [0] + list(
            accumulate(
                r - l + 1
                for r, l in enumerate(min_lefts)
            )
        )

        rslt: list[int] = []
        for l, r in queries:
            m = min(r, max_rights[l])
            size = m - l + 1

            # candidate substrings from l to m
            curr = size * (size + 1) // 2

            # candidate substrings from m to r
            curr += pre_sums[r + 1] - pre_sums[m + 1]

            rslt.append(curr)

        return rslt


print(Solution().count_k_constraint_substrings(
    "010101", 1, [[0, 5], [1, 4], [2, 3]]))
