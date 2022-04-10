"""
https://leetcode.com/problems/employee-importance/
"""


from typing import List


from test_helper import Employee


class Solution:
    def getImportance(self, employees: List[Employee], id: int) -> int:
        memo = {employee.id: employee for i, employee in enumerate(employees)}
        if id not in memo:
            return 0

        sumImportanace, currEmployess = 0, [memo[id]]
        while currEmployess:
            nextEmployees = []
            for employee in currEmployess:
                sumImportanace += employee.importance
                nextEmployees.extend(memo[i] for i in employee.subordinates)

            currEmployess = nextEmployees

        return sumImportanace


print(Solution().getImportance([[1, 2, [2]], [2, 3, []]], 2))
