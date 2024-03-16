"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram-ii/description/
"""


from collections import Counter


class Solution:
    """
    Solution
    """

    def min_steps(self, s: str, t: str) -> int:
        """
        min_steps
        """
        cs, ct = Counter(s), Counter(t)
        steps = 0
        for k, v in cs.items():
            steps += abs(v - ct[k])
            del ct[k]

        for k, v in ct.items():
            steps += abs(v - cs[k])

        return steps
