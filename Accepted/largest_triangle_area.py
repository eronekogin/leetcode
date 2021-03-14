"""
https://leetcode.com/problems/largest-triangle-area/
"""


from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        """
        Heron's formula. 
        """
        maxArea = -1
        for p1, p2, p3 in combinations(points, 3):
            a = ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
            b = ((p1[0] - p3[0]) ** 2 + (p1[1] - p3[1]) ** 2) ** 0.5
            c = ((p2[0] - p3[0]) ** 2 + (p2[1] - p3[1]) ** 2) ** 0.5
            p = (a + b + c) / 2
            maxArea = max(maxArea, p * (p - a) * (p - b) * (p - c))

        return maxArea ** 0.5

    def largestTriangleArea2(self, points: list[list[int]]) -> float:
        """
        Shoelace formula. 
        """
        maxArea = -1
        for p1, p2, p3 in combinations(points, 3):
            s1 = p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
            s2 = p1[1] * p2[0] + p2[1] * p3[0] + p3[1] * p1[0]
            maxArea = max(maxArea, abs(s1 - s2))

        return maxArea / 2
