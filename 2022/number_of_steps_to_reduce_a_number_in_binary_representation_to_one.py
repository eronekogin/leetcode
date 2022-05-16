"""
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
"""


class Solution:
    def numSteps(self, s: str) -> int:
        carry = 0
        stepCnt = 0
        for i in range(len(s) - 1, 0, -1):
            if int(s[i]) + carry == 1:  # Odd number.
                carry = 1
                stepCnt += 1  # Extra add 1 step.

            stepCnt += 1  # Divide by 2 for even number.

        return stepCnt + carry


print(Solution().numSteps('1101'))
