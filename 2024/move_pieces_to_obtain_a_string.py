"""
https://leetcode.com/problems/move-pieces-to-obtain-a-string/description/
"""


class Solution:
    """
    Solution
    """

    def can_change(self, start: str, target: str) -> bool:
        """
        can change
        """
        n = len(start)
        i = j = 0

        while i < n or j < n:
            while i < n and start[i] == '_':
                i += 1

            while j < n and target[j] == '_':
                j += 1

            if i == n or j == n:
                return i == j == n

            if start[i] != target[j]:
                return False

            if start[i] == 'L':
                if i < j:
                    return False
            else:
                if i > j:
                    return False

            i += 1
            j += 1

        return True
