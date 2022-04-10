"""
https://leetcode.com/problems/self-dividing-numbers/
"""


from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rslt = []
        for num in range(left, right + 1):
            currNum, isCandidate = num, True
            while currNum and isCandidate:
                currNum, r = divmod(currNum, 10)
                if not r or num % r:
                    isCandidate = False

            if isCandidate:
                rslt.append(num)

        return rslt
