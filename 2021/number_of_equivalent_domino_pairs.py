"""
https://leetcode.com/problems/number-of-equivalent-domino-pairs/
"""


from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        cnt = Counter()
        for a, b in dominoes:
            cnt[(a, b)] += 1

        pairCnt = 0
        visited = set()
        for (a, b) in cnt:
            if (a, b) not in visited:
                if a != b:
                    n = cnt[(a, b)] + cnt[(b, a)]
                else:
                    n = cnt[(a, b)]

                if n > 1:  # Must have at least two items to form a pair.
                    pairCnt += (n * (n - 1)) >> 1  # n! / ((n - 2)! * 2!)
                    visited.add((a, b))
                    visited.add((b, a))

        return pairCnt


print(Solution().numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]))
