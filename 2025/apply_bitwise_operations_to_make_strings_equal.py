"""
https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/description/
"""


class Solution:
    """
    Solution
    """

    def make_strings_equal(self, s: str, target: str) -> bool:
        """
        Enumerate the values for s[i] and s[j]:
            (0, 0) -> (0, 0)
            (1, 0) -> (1, 1)
            (0, 1) -> (1, 1)
            (1, 1) -> (1, 0)

        Continue to sunmmrize:
            All 0 string can not change.
            Any other strings can transform from each other.    
        """
        return ('1' in s) == ('1' in target)
