"""
https://leetcode.com/problems/buddy-strings/
"""


from collections import Counter


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """
        1. If A and B have different length, no swap.
        2. If A == B, could only swap on the same characters.
        3. If A != B, check any difference pairs, where we should only have
            two such pairs with the value corresponded to each other.
        """
        if len(A) != len(B):
            return False

        if A == B:
            return len(set(A)) < len(A)

        diffs = [(a, b) for a, b in zip(A, B) if a != b]
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]


print(Solution().buddyStrings('abc', 'acd'))
