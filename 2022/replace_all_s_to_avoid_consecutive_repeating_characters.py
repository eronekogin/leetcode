"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""


from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        originalChars = list(s)
        i, n = 0, len(s)
        while i < n:
            if originalChars[i] == '?':
                start = i - 1
                while i + 1 < n and originalChars[i + 1] == '?':
                    i += 1

                end = i + 1

                startChar = 'a'
                if start >= 0:
                    startChar = originalChars[start]

                endChar = 'z'
                if end < n:
                    endChar = originalChars[end]

                for j in range(start + 1, end):
                    for c in ascii_lowercase:
                        if c != startChar and c != endChar:
                            originalChars[j] = c
                            startChar = c
                            break

                i = end
            else:
                i += 1

        return ''.join(originalChars)
