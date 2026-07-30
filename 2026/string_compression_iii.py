"""
https://leetcode.com/problems/string-compression-iii/description/
"""


class Solution:
    """
    Solution
    """

    def compressed_string(self, word: str) -> str:
        """
        compressed string
        """
        parts: list[str] = []
        prev = word[0]
        cnt = 0
        for c in word + '#':
            if c == prev:
                if cnt < 9:
                    cnt += 1
                    continue

            parts.append(str(cnt) + prev)
            prev = c
            cnt = 1

        return ''.join(parts)


print(Solution().compressed_string('aaaaaaaaaaaaaabb'))
