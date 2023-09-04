"""
https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
"""


class Solution:
    def numberOfWeeks(self, milestones: list[int]) -> int:
        total = sum(milestones)
        maxMilestone = max(milestones)

        if total - maxMilestone >= maxMilestone:
            return total
        
        return 2 * (total - maxMilestone) + 1


    
print(Solution().numberOfWeeks([5,7,5,7,9,7]))
        