"""
https://leetcode.com/problems/number-of-wonderful-substrings/
"""


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        OFFSET = ord('a')
        maskCnt = [1] + [0] * (1 << 10)
        wonderfulSubStrings = 0
        currMask = 0

        for c in word:
            currMask ^= 1 << (ord(c) - OFFSET)

            # Find all substrings from previous occurring mask that has the same value as currMask,
            # which means the strings between them contain even number of chars.
            wonderfulSubStrings += maskCnt[currMask]

            # Try to flip one char among the current mask to make it at most one char with odd number.
            wonderfulSubStrings += sum(
                maskCnt[currMask ^ (1 << i)]
                for i in range(10)
            )

            maskCnt[currMask] += 1
        
        return wonderfulSubStrings


print(Solution().wonderfulSubstrings('aba'))