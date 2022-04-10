"""
https://leetcode.com/problems/advantage-shuffle/
"""


from collections import defaultdict


class Solution:
    def advantageCount(self, A: list[int], B: list[int]) -> list[int]:
        """
        For sorted A and B, start scanning from the end, and if B[-1] < A[-1],
        pair the target item from A.
        """
        sa = sorted(A)
        assigned = defaultdict(list)
        for b in reversed(sorted(B)):
            if b < sa[-1]:
                assigned[b].append(sa.pop())

        return [(assigned[b] or sa).pop() for b in B]
