"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
"""


class Solution:
    def minFlips(self, s: str) -> int:
        windowSize = len(s)
        if windowSize <= 1:
            return 0
        
        if windowSize & 1:  # Odd length.
            t = s + s
        else:
            t = s
        
        t1 = ''.join('1' if i & 1 else '0' for i in range(len(t)))
        t2 = ''.join('0' if i & 1 else '1' for i in range(len(t)))

        d1 = d2 = 0
        start = end = 0
        minFlips = windowSize
        while end < len(t):
            if t[end] != t1[end]:
                d1 += 1
            
            if t[end] != t2[end]:
                d2 += 1
            
            if end - start + 1 < windowSize:
                end += 1
            else:
                minFlips = min(minFlips, d1, d2)
                if t[start] != t1[start]:
                    d1 -= 1
                
                if t[start] != t2[start]:
                    d2 -= 1
                
                start += 1
                end += 1
        
        return minFlips

print(Solution().minFlips('111000'))