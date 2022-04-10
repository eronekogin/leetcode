"""
https://leetcode.com/problems/expression-add-operators/
"""


from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []

        rslt, maxLen = [], len(num)

        def calc(start: int, currPath: List[str], currVal: int, preVal: int):
            if start == maxLen and target == currVal:
                rslt.append(''.join(currPath))
                return

            for i in range(start, maxLen):
                # Prevent '0...' sequence to be recognized as a number.
                if i != start and num[start] == '0':
                    break

                nextStart = i + 1
                opStr = num[start: nextStart]
                opVal = int(opStr)
                if not start:  # The first number.
                    calc(nextStart, currPath + [opStr], opVal, opVal)
                else:
                    calc(nextStart, currPath + ['+', opStr],
                         currVal + opVal, opVal)
                    calc(nextStart, currPath + ['-', opStr],
                         currVal - opVal, -opVal)
                    calc(nextStart, currPath + ['*', opStr],
                         currVal - preVal + opVal * preVal, opVal * preVal)

        calc(0, [], 0, 0)
        return rslt
