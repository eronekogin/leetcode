"""
https://leetcode.com/problems/fruit-into-baskets/
"""


class Solution:
    def totalFruit(self, tree: list[int]) -> int:
        """
        The problem description is too vague: it simply wants to find the
        longest subarray of the input list with no more than 2 distinct
        numbers, thus we could use sliding window to handle such problems.
        """
        cnt = {}
        start = 0
        for end, c in enumerate(tree):
            cnt[c] = cnt.get(c, 0) + 1
            if len(cnt) > 2:
                cnt[tree[start]] -= 1
                if cnt[tree[start]] == 0:
                    del cnt[tree[start]]

                start += 1

        return end - start + 1
