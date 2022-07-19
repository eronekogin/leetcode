"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""


class Solution:
    def average(self, salary: list[int]) -> float:
        maxSalary, minSalary = float('-inf'), float('inf')
        totalSalary = 0
        for s in salary:
            maxSalary = max(maxSalary, s)
            minSalary = min(minSalary, s)
            totalSalary += s

        return (totalSalary - maxSalary - minSalary) / (len(salary) - 2)
