"""
https://leetcode.com/problems/describe-the-painting/
"""


class Solution:
    def splitPainting(self, segments: list[list[int]]) -> list[list[int]]:
        memo: dict[int, int] = {}
        for start, end, color in segments:
            memo[start] = memo.get(start, 0) + color
            memo[end] = memo.get(end, 0) - color
        
        rslt: list[list[int]] = []
        prev, color = -1, 0
        for curr in sorted(memo):
            if color:
                rslt.append([prev, curr, color])
            
            color += memo[curr]
            prev = curr
        
        return rslt



