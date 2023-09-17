"""
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
"""


from bisect import bisect_right


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        memo = [float('-inf')]
        rslt = []
        for num in obstacles:
            i = bisect_right(memo, num)
            if i == len(memo):
                rslt.append(len(memo))
                memo.append(num)
            else:
                rslt.append(i)
                memo[i] = num
        
        return rslt


        