"""
https://leetcode.com/problems/hash-divided-string/description/
"""


class Solution:
    """
    Solution
    """
    def string_hash(self, s: str, k: int) -> str:
        """
        string hash
        """
        def calc_hash(start: int, end: int) -> str:
            char_sum = 0
            for i in range(start, end):
                char_sum += ord(s[i]) - offset

            return chr(offset + char_sum % 26)

        offset = ord('a')
        return ''.join(calc_hash(i, i + k) for i in range(0, len(s), k))


print(Solution().string_hash('abcd', 2))
