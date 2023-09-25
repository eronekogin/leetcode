"""
https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/
"""


class Solution:
    def minTimeToType(self, word: str) -> int:
        preChar = 'a'
        seconds = 0
        for c in word:
            distance = abs(ord(c) - ord(preChar))
            moveSeconds = min(distance, 26 - distance)
            seconds += moveSeconds + 1  # Type takes 1 second.
            preChar = c
        
        return seconds