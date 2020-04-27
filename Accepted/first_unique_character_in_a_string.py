"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        memo = Counter(s)
        for i, c in enumerate(s):
            if memo[c] == 1:
                return i

        return -1  # Not found.


print(Solution().firstUniqChar('leetcode'))
