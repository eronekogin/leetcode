"""
https://leetcode.com/problems/make-number-of-distinct-characters-equal/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def is_it_possible(self, word1: str, word2: str) -> bool:
        """
        is it possible
        """
        def add_and_remove(cnt: Counter, to_add: str, to_remove: str):
            cnt[to_add] += 1
            cnt[to_remove] -= 1

            if cnt[to_remove] <= 0:
                del cnt[to_remove]

        cnt1, cnt2 = Counter(word1), Counter(word2)
        s1, s2 = list(cnt1.keys()), list(cnt2.keys())
        for c1 in s1:
            for c2 in s2:
                add_and_remove(cnt1, c2, c1)
                add_and_remove(cnt2, c1, c2)

                if len(cnt1) == len(cnt2):
                    return True

                add_and_remove(cnt1, c1, c2)
                add_and_remove(cnt2, c2, c1)

        return False
