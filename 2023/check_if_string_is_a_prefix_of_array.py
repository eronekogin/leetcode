"""
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
"""


class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        iw = ic = 0
        for c in s:
            if iw == len(words) or c != words[iw][ic]:
                return False
            
            ic += 1
            if ic == len(words[iw]):
                ic = 0
                iw += 1
        
        return ic == 0
        

