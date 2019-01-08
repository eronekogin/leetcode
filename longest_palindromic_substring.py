"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s


textList = ['babad', 'cbbd']
s = Solution()

for text in textList:
    print('{0} -> {1}'.format(text, s.longestPalindrome(text)))
