"""
https://leetcode.com/problems/strange-printer/
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        """
        Bottom up DFS with pre-processing.
        """
        def compress(s: str) -> str:
            """
            Compress the input string to reduce consecutive same chars
            into 1 char only.
            """
            i, n, rslt = 0, len(s), []
            while i < n:
                while i + 1 < n and s[i + 1] == s[i]:
                    i += 1

                rslt.append(s[i])
                i += 1

            return ''.join(rslt)

        def do(start: int, end: int) -> int:
            if end < start:
                return 0

            if end == start:
                return 1

            if (start, end) not in memo:
                cost = do(start, end - 1) + 1  # Simply append the last char.

                # Check if the last char also exists in the previous part of
                # the string. If so, we could print the last char together
                # with this char to reduce 1 print step.
                for i in range(start, end):
                    if cs[i] == cs[end]:
                        cost = min(cost, do(start, i - 1) + do(i, end - 1))

                memo[(start, end)] = cost

            return memo[(start, end)]

        memo = {}
        cs = compress(s)
        return do(0, len(cs) - 1)


print(Solution().strangePrinter('aaabbb'))
print(Solution().strangePrinter('aabbc'))
