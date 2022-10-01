"""
https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
"""


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(start: int, seen: set[str]) -> None:
            if start == N:  # Split is done.
                self.maxUniqueSubString = max(
                    self.maxUniqueSubString, len(seen))

                return

            for end in range(start + 1, N + 1):
                subStr = s[start: end]
                if subStr not in seen:
                    seen.add(subStr)
                    split(end, seen)
                    seen.remove(subStr)

        self.maxUniqueSubString = 1
        N = len(s)
        split(0, set())
        return self.maxUniqueSubString


print(Solution().maxUniqueSplit("ababccc"))
