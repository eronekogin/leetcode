"""
https://leetcode.com/problems/count-artifacts-that-can-be-extracted/description/
"""


class Solution:
    """
    Solution
    """

    def dig_artifacts(self, n: int, artifacts: list[list[int]], dig: list[list[int]]) -> int:
        """
        dig artifacts
        """
        can_dig = {(x, y) for x, y in dig}
        cnt = 0
        for r1, c1, r2, c2 in artifacts:
            if all(
                (r, c) in can_dig
                for r in range(r1, r2 + 1)
                for c in range(c1, c2 + 1)
            ):
                cnt += 1

        return cnt
