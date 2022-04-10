"""
https://leetcode.com/problems/implement-strstr/
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleLen, haystackLen = len(needle), len(haystack)

        if needleLen == 0:  # Needle is an empty string.
            return 0

        i = 0

        while i < haystackLen and haystackLen - i >= needleLen:
            if haystack[i] == needle[0]:
                j = 1

                while j < needleLen:
                    if haystack[i + j] != needle[j]:
                        break  # No match.

                    j += 1

                if j == needleLen:  # Found the first occurrence.
                    return i

            i += 1  # Advance i if no match is found.

        return -1  # When coming here, no match is found.


print(Solution().strStr('mississippi', 'issip'))
