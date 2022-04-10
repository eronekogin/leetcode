"""
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        total = len(s)
        
        if total < 1:
            return s
        
        start = end = 0

        for i in range(total):
            # Try to expand from char itself.
            l = r = i
            while l > -1 and r < total and s[l] == s[r]:
                l -= 1
                r += 1
            oddLen = r - l - 1  # (r-1) - (l+1) + 1

            # Try to expand from adjacent char.
            l = i
            r = i + 1
            while l > -1 and r < total and s[l] == s[r]:
                l -= 1
                r += 1
            evenLen = r - l - 1  # (r-1) - (l+1) + 1

            rsltLen = max(oddLen, evenLen)

            if rsltLen > end - start:
                start = i - ((rsltLen - 1) >> 1)  # For odd case
                end = i + (rsltLen >> 1)  # For even case
        
        return s[start:end+1]


textList = ['abb']
s = Solution()

for text in textList:
    print('{0} -> {1}'.format(text, s.longestPalindrome(text)))
