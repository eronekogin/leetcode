"""
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/
"""


class Solution:
    def minimumEffort(self, tasks: list[list[int]]) -> int:
        """
        Suppose we have n invenstors, each investor will invest actual money
        to your company and he thinks the company worths minimum money.

        So if currently we have minimum - actual money, the investor will just
        invest actual money.

        Then we sort the tasks by m - a in ascending order, and at the end
        our current money is the energy needed to satisfy all investors.
        """
        sortedTasks = sorted(tasks, key=lambda x: x[1] - x[0])
        currEnergy = 0
        for a, m in sortedTasks:
            currEnergy = max(currEnergy + a, m)

        return currEnergy
