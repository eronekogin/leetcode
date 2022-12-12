"""
https://leetcode.com/problems/reformat-phone-number/
"""


class Solution:
    def reformatNumber(self, number: str) -> str:
        rslt = number.replace(' ', '').replace('-', '')
        N = len(rslt)
        splitted: list[str] = []

        if N % 3 == 1:
            maxRemainLen = 4
        else:
            maxRemainLen = N % 3

        for i in range(0, N - maxRemainLen, 3):
            splitted.append(rslt[i: i + 3])

        if maxRemainLen > 0:
            if maxRemainLen == 4:
                splitted.append(rslt[-4:-2])

            splitted.append(rslt[-2:])

        return '-'.join(splitted)


print(Solution().reformatNumber('123 4-567'))
