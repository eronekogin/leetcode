"""
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


class Solution:
    def maxScore(self, s: str) -> int:
        zeros = 1 if s[0] == '0' else 0
        ones = 0
        for i in range(1, len(s)):
            if s[i] == '1':
                ones += 1

        maxScore = zeros + ones
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            maxScore = max(maxScore, ones + zeros)

        return maxScore


print(Solution().maxScore("011101"))
