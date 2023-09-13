"""
https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/
"""


class Solution:
    def maxProduct(self, s: str) -> int:
        def fn(s): 
            """Return length of longest odd palindroms ending at index."""
            ans = [1]*n
            hlen = [0]*n # half-length
            center = right = 0 
            for i in range(n): 
                if i < right: hlen[i] = min(right - i, hlen[2*center - i])
                while 0 <= i-1-hlen[i] and i+1+hlen[i] < len(s) and s[i-1-hlen[i]] == s[i+1+hlen[i]]: 
                    hlen[i] += 1
                    ans[i+hlen[i]] = max(ans[i+hlen[i]], 2*hlen[i]+1)
                if right < i+hlen[i]: center, right = i, i+hlen[i]
            for i in range(1, n): ans[i] = max(ans[i-1], ans[i])
            return ans
        
        n = len(s)
        prefix = fn(s)
        suffix = fn(s[::-1])
        return max(prefix[i-1]*suffix[~i] for i in range(1, n))