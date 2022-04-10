"""
https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""


class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        each, r = divmod(total, 3)
        if r:
            return False

        currSum = cnt = 0
        for num in arr:
            currSum += num
            if currSum == each:
                cnt += 1
                currSum = 0

            if cnt == 3:
                return True

        return False


print(Solution().canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]))
