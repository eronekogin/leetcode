"""
https://leetcode.com/problems/substring-with-largest-variance/description/
"""


from collections import Counter
from itertools import permutations


class Solution:
    """
    Solutionm
    """

    def largest_variance(self, s: str) -> int:
        """
        largest variance
        """
        cnt = Counter(s)
        max_variance = 0

        for a, b in permutations(cnt, 2):
            curr_variance = 0
            has_a = has_b = False
            remain_a, remain_b = cnt[a], cnt[b]

            for c in s:
                if c != a and c != b:
                    continue

                if curr_variance < 0 and remain_a > 0 and remain_b > 0:
                    curr_variance = 0
                    has_a = has_b = False

                if c == a:
                    curr_variance += 1
                    has_a = True
                    remain_a -= 1
                else:
                    curr_variance -= 1
                    has_b = True
                    remain_b -= 1

                if has_a and has_b:
                    max_variance = max(max_variance, curr_variance)

        return max_variance
