"""
https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/
"""


class Solution:
    """
    Solution
    """

    def is_substring_present(self, s: str) -> bool:
        """
        is substring present
        """
        seen: set[str] = set()
        n = len(s)
        for i in range(n - 1):
            seen.add(s[i: i + 2])

        rs = s[::-1]
        for i in range(n - 1):
            if rs[i: i + 2] in seen:
                return True

        return False


print(Solution().is_substring_present('leetcode'))
