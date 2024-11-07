"""
https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/
"""


class Solution:
    """
    Solution
    """

    def robot_with_string(self, s: str) -> str:
        """
        robot with string
        """
        n = len(s)
        rslt: list[str] = []
        stack: list[str] = []
        min_suffix: list[str] = [s[-1]] * n

        for i in range(n - 2, -1, -1):
            min_suffix[i] = min(s[i], min_suffix[i + 1])

        for i, c in enumerate(s):
            stack.append(c)
            while i + 1 < n and stack and min_suffix[i + 1] >= stack[-1]:
                rslt.append(stack.pop())

        return ''.join(rslt + stack[::-1])


print(Solution().robot_with_string("bydizfve"))
