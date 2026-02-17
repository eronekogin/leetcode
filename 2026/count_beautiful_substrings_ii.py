"""
https://leetcode.com/problems/count-beautiful-substrings-ii/description/
"""


from collections import Counter
from itertools import count


class Solution:
    """
    Docstring for Solution
    """

    def beautiful_substrings(self, s: str, k: int) -> int:
        """
        Suppose the minimum length of substring that has
        vowels = consonants and length is l, then the other
        condition become (l // 2) * (l // 2) % k == 0, which
        is (l * l) % (4 * k) == 0

        Then we find such l, and consider the prefix sums of
        difference between the vowels and consonants, suppose
        diff is d and if the same d occurs later, then every
        time a d occurs, it can form a new substring between
        i % l and i, such that its diff sum is zero.
        """
        l = next(i for i in count(1) if (i * i) % k == 0) * 2
        seen = [Counter() for i in range(l)]
        seen[-1][0] = 1
        cnt = 0
        d = 0
        vowels = set('aeiou')

        for i, c in enumerate(s):
            if c in vowels:
                d += 1
            else:
                d -= 1

            cnt += seen[i % l][d]
            seen[i % l][d] += 1

        return cnt
