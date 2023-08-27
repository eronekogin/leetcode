"""
https://leetcode.com/problems/number-of-visible-people-in-a-queue/
"""


class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        N = len(heights)
        rslt = [0] * N
        stack: list[int] = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] <= h:
                # The person at the top of the stack can see the current person.
                # And the current person blocked the top stack person to see any other person
                # after the current person, so we completed processing of the top stack person.
                rslt[stack.pop()] += 1
            
            if stack:
                # The person at the top of the stack now has a height >= current person's height,
                # which means he can see the current person, so we increase the seeing people number.
                rslt[stack[-1]] += 1
            
            stack.append(i)
        
        return rslt
