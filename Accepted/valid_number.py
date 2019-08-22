"""
https://leetcode.com/problems/valid-number/
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Use DFA=Deterministic Finite Automation. The available triggers
        could be ' ', '+', '-', '0-9', 'e', '.'.
        """
        refs = {'.': 'd', 'e': 'e', '+': 's', '-': 's', ' ': 'b'}
        for c in '0123456789':
            refs[c] = 'n'

        states = [
            {'b': 0, 's': 1, 'd': 3, 'n': 2},
            {'n': 2, 'd': 3},
            {'n': 2, 'b': 8, 'e': 5, 'd': 4},  # Valid number.
            {'n': 4},
            {'n': 4, 'e': 5, 'b': 8},  # Valid number.
            {'s': 6, 'n': 7},
            {'n': 7},
            {'n': 7, 'b': 8},  # Valid number.
            {'b': 8}  # Valid number.
        ]

        currState = 0
        for c in s:
            if c not in refs:
                return False  # Invalid char in string.

            if refs[c] not in states[currState]:
                return False  # Invalid trigger for the current state.

            currState = states[currState][refs[c]]

        return currState in [2, 4, 7, 8]


print(Solution().isNumber('.1'))
