"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1

        l, r = 0, N - 1
        while l < r and s[l] == s[r]:
            while l + 1 < r and s[l + 1] == s[l]:
                l += 1

            while r - 1 > l and s[r - 1] == s[r]:
                r -= 1

            l += 1
            r -= 1

        return r - l + 1


print(Solution().minimumLength('aabccabba'))
