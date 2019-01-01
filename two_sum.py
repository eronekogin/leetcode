"""
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        chkDict = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            chkNum = target - num
            rsltPos = chkDict.get(chkNum)
            
            if rsltPos is not None and rsltPos != i:
                return [rsltPos, i]
            
            chkDict[num] = i
