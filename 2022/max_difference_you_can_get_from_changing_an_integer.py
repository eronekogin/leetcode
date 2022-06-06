"""
https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        maxNum = minNum = str(num)
        for c in maxNum:
            if c != '9':
                maxNum = maxNum.replace(c, '9')
                break

        if minNum[0] != '1':
            minNum = minNum.replace(minNum[0], '1')
        else:
            for c in minNum:
                if c not in '01':
                    minNum = minNum.replace(c, '0')
                    break

        return int(maxNum) - int(minNum)


print(Solution().maxDiff(123456))
