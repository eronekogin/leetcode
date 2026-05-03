"""
https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/
"""


class Solution:
    """
    Solution
    """

    def count_prefix_suffix_pairs(self, words: list[str]) -> int:
        """
        count prefix suffix pairs
        """
        def check(s1: str, s2: str) -> bool:
            return s2.startswith(s1) and s2.endswith(s1)

        return sum(
            check(words[i], words[j])
            for i in range(len(words))
            for j in range(i + 1, len(words))
        )
