"""
https://leetcode.com/problems/occurrences-after-bigram/
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        words = text.split()
        rslt = []
        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                rslt.append(words[i + 2])

        return rslt


print(Solution().findOcurrences(
    'alice is a good girl she is a good student', 'a', 'good'))
